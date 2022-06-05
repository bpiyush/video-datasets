# Video Datasets
Common place to download, pre-process and standardise video datasets.


## Setup

Create a `conda` environment with the following packages:
```bash
conda create -y -n base-video python=3.9
conda activate base-video
conda install -y -c conda-forge ffmpeg
pip install opencv-python av
pip install numpy pillow matplotlib pandas scipy PyYAML tqdm termcolor natsort ftfy regex
```

## Downloads

### [MSR-VTT](https://www.microsoft.com/en-us/research/publication/msr-vtt-a-large-video-description-dataset-for-bridging-video-and-language/)

* Download splits and raw videos
  ```bash
  bash MSRVTT/download_data.sh
  ```
  :hourglass: This takes about 10-30 minutes (depending on your internet connection).