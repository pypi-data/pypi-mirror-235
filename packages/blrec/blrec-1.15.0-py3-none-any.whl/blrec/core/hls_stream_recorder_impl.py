import logging
from typing import Optional

from reactivex.scheduler import NewThreadScheduler

from blrec.bili.live import Live
from blrec.bili.typing import QualityNumber
from blrec.flv import operators as flv_ops
from blrec.flv.metadata_dumper import MetadataDumper
from blrec.hls import operators as hls_ops
from blrec.utils import operators as utils_ops

from . import operators as core_ops
from .stream_recorder_impl import StreamRecorderImpl

__all__ = ('HLSStreamRecorderImpl',)


logger = logging.getLogger(__name__)


class HLSStreamRecorderImpl(StreamRecorderImpl):
    def __init__(
        self,
        live: Live,
        out_dir: str,
        path_template: str,
        *,
        quality_number: QualityNumber = 10000,
        buffer_size: Optional[int] = None,
        read_timeout: Optional[int] = None,
        disconnection_timeout: Optional[int] = None,
        filesize_limit: int = 0,
        duration_limit: int = 0,
    ) -> None:
        super().__init__(
            live=live,
            out_dir=out_dir,
            path_template=path_template,
            stream_format='fmp4',
            recording_mode='standard',
            quality_number=quality_number,
            buffer_size=buffer_size,
            read_timeout=read_timeout,
            disconnection_timeout=disconnection_timeout,
            filesize_limit=filesize_limit,
            duration_limit=duration_limit,
        )

        self._playlist_fetcher = hls_ops.PlaylistFetcher(self._live, self._session)
        self._playlist_resolver = hls_ops.PlaylistResolver(self._stream_url_resolver)
        self._segment_fetcher = hls_ops.SegmentFetcher(
            self._live, self._session, self._stream_url_resolver
        )
        self._segment_remuxer = hls_ops.SegmentRemuxer(live)

        self._prober = hls_ops.Prober()
        self._dl_statistics = core_ops.SizedStatistics()

        self._segment_parser = hls_ops.SegmentParser()
        self._analyser = flv_ops.Analyser()
        self._injector = flv_ops.Injector(self._metadata_provider)
        self._join_point_extractor = flv_ops.JoinPointExtractor()
        self._limiter = flv_ops.Limiter(filesize_limit, duration_limit)
        self._cutter = flv_ops.Cutter()
        self._dumper = flv_ops.Dumper(self._path_provider, buffer_size)
        self._metadata_dumper = MetadataDumper(
            self._dumper, self._analyser, self._join_point_extractor
        )

        self._recording_monitor = core_ops.RecordingMonitor(
            live, lambda: self._analyser.duration
        )

        self._prober.profiles.subscribe(self._on_profile_updated)
        self._dumper.file_opened.subscribe(self._on_video_file_opened)
        self._dumper.file_closed.subscribe(self._on_video_file_closed)
        self._recording_monitor.interrupted.subscribe(self._on_recording_interrupted)
        self._recording_monitor.recovered.subscribe(self._on_recording_recovered)

    @property
    def buffer_size(self) -> int:
        return self._dumper.buffer_size

    @buffer_size.setter
    def buffer_size(self, value: int) -> None:
        self._dumper.buffer_size = value

    @property
    def recording_path(self) -> Optional[str]:
        return self._dumper.path

    @property
    def filesize_limit(self) -> int:
        return self._limiter.filesize_limit

    @filesize_limit.setter
    def filesize_limit(self, value: int) -> None:
        self._limiter.filesize_limit = value

    @property
    def duration_limit(self) -> int:
        return self._limiter.duration_limit

    @duration_limit.setter
    def duration_limit(self, value: int) -> None:
        self._limiter.duration_limit = value

    @property
    def metadata(self) -> Optional[flv_ops.MetaData]:
        try:
            return self._analyser.make_metadata()
        except Exception:
            return None

    def can_cut_stream(self) -> bool:
        return self._cutter.can_cut_stream()

    def cut_stream(self) -> bool:
        return self._cutter.cut_stream()

    def _on_start(self) -> None:
        self._metadata_dumper.enable()

    def _on_stop(self) -> None:
        self._metadata_dumper.disable()

    def _run(self) -> None:
        self._subscription = (
            self._stream_param_holder.get_stream_params()  # type: ignore
            .pipe(
                self._stream_url_resolver,
                self._playlist_fetcher,
                self._recording_monitor,
                self._connection_error_handler,
                self._request_exception_handler,
                self._playlist_resolver,
                utils_ops.observe_on_new_thread(
                    queue_size=60, thread_name=f'SegmentFetcher::{self._live.room_id}'
                ),
                self._segment_fetcher,
                self._dl_statistics,
                self._prober,
                utils_ops.observe_on_new_thread(
                    queue_size=10, thread_name=f'StreamRecorder::{self._live.room_id}'
                ),
                self._segment_remuxer,
                self._segment_parser,
                flv_ops.process(),
                self._cutter,
                self._limiter,
                self._join_point_extractor,
                self._injector,
                self._analyser,
                self._dumper,
                self._rec_statistics,
                self._progress_bar,
                self._exception_handler,
            )
            .subscribe(
                on_completed=self._on_completed,
                scheduler=NewThreadScheduler(self._thread_factory('HLSStreamRecorder')),
            )
        )
