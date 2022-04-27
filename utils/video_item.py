"""
Class to handle a single video object.
"""

from genericpath import exists
import numpy as np
import torch
import torchvision
import av
import random

from torchvision.transforms import Compose, ToTensor, Normalize

from utils.video_transforms import ClipToTensor, Resize



def av_load_video(container, video_fps=None, start_time=0, duration=None):
    """Helper function to load video."""
    video_stream = container.streams.video[0]
    _ss = video_stream.start_time * video_stream.time_base
    _dur = video_stream.duration * video_stream.time_base
    _ff = _ss + _dur
    _fps = video_stream.average_rate

    if video_fps is None:
        video_fps = _fps

    if duration is None:
        duration = _ff - start_time

    # Figure out which frames to decode
    iterator = np.arange(start_time, min(start_time + duration - 0.5/_fps, _ff), 1./video_fps)
    outp_times = [t for t in iterator][:int(duration*video_fps)]
    outp_vframes = [int((t - _ss) * _fps) for t in outp_times]
    start_time = outp_vframes[0] / float(_fps)

    # Fast forward
    container.seek(int(start_time * av.time_base))

    # Decode snippet
    frames = []
    for frame in container.decode(video=0):
        if len(frames) == len(outp_vframes):
            break   # All frames have been decoded
        frame_no = frame.pts * frame.time_base * _fps
        if frame_no < outp_vframes[len(frames)]:
            continue    # Not the frame we want

        # Decode
        pil_img = frame.to_image()
        while frame_no >= outp_vframes[len(frames)]:
            frames += [pil_img]
            if len(frames) == len(outp_vframes):
                break   # All frames have been decoded

    return frames, video_fps, start_time


class VideoItem:
    """Class to handle a single video object."""

    def __init__(self, video_path: str) -> None:
        assert isinstance(video_path, str)
        assert video_path.endswith(".mp4") or video_path.endswith(".mkv")
        assert exists(video_path), "Video file does not exist: {}".format(video_path)
        self.video_path = video_path
        self.video_container = av.open(video_path)

        self.video_transform = [
            Resize(270),
            ClipToTensor(),
        ]
    
    def _get_time_lims(self, video_ctr):
        """Returns start and end time of the video."""
        video_st, video_ft = None, None

        video_stream = video_ctr.streams.video[0]
        tbase = video_stream.time_base
        video_st = video_stream.start_time * tbase
        video_dur = video_stream.duration * tbase
        video_ft = video_st + video_dur

        return video_st, video_ft
    
    def _get_duration(self):
        """Returns the duration of the video."""
        video_st, video_ft = self._get_time_lims(self.video_container)
        return float(video_ft - video_st)

    def _sample_snippet(self, video_clip_duration):
        """
        Samples a snippet of duration `video_clip_duration` (secs) from
        the range [t_{s}, t_{f}] within the video. By default, the range
        is [0, video_duration].
        """
        video_st, video_ft = self._get_time_lims(self.video_container)
        video_duration = video_ft - video_st

        if video_clip_duration > video_duration:
            return 0., video_duration
        else:
            # video_clip_duration <= video_duration
            min_d, max_d = video_clip_duration, min(video_clip_duration, video_duration)
            duration = random.uniform(min_d, max_d)
            sample_ss_v = random.uniform(video_st, video_ft - duration)
            return sample_ss_v, duration

    def _get_clip(self, clip_start_time, clip_duration, video_fps=None):
        
        sample = {}

        frames, fps, start_time = av_load_video(
            self.video_container,
            video_fps=video_fps,
            start_time=clip_start_time,
            duration=clip_duration,
        )
        if self.video_transform is not None:
            for t in self.video_transform:
                frames = t(frames)

        sample['frames'] = frames
        sample['fps'] = float(fps)
        sample['start_time'] = start_time
        sample['duration'] = clip_duration

        return sample


if __name__ == "__main__":
    # video_path = "/var/scratch/pbagad/datasets/activitynet-1.3/v1-3/test/v_zVRajE-LL4I.mp4"
    video_path = "/ssd/pbagad/datasets/DiDeMo/videos/57959349@N00_3017931116_62f4d0a592.mov.mp4"
    print("Loading video at {}".format(video_path))
    video_item = VideoItem(video_path)

    video_container = video_item.video_container

    video_st, video_ft = video_item._get_time_lims(video_container)
    video_duration = float(video_ft - video_st)
    print("The video duration is: {}".format(video_duration))

    sample_ss_v, duration = video_item._sample_snippet(10.)
    clip = video_item._get_clip(sample_ss_v, duration)

    clip = video_item._get_clip(2.31, 1.)
    assert clip["frames"].shape == torch.Size([3, 29, 270, 360])
    assert clip["duration"] == 1.
    assert clip["start_time"] == 2.3023000000000002
