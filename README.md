# Video Datasets
Common place to download, pre-process and standardise video datasets.


## Setup

Create a `conda` environment with the following packages:
```zsh
conda create -y -n base-video python=3.9
conda activate base-video
conda install -y -c conda-forge ffmpeg
pip install opencv-python av
pip install numpy pillow matplotlib pandas scipy PyYAML tqdm termcolor natsort ftfy regex ipython jupyterlab ipdb seaborn

# for latex fonts in matplotlib
conda install -y -c conda-forge texlive-core
```

Set `PYTHONPATH` as the repo-folder:
```zsh
cd /path/to/video-datasets
export PYTHONPATH=$PWD
```

## Downloads

### [MSR-VTT](https://www.microsoft.com/en-us/research/publication/msr-vtt-a-large-video-description-dataset-for-bridging-video-and-language/)

* Download splits and raw videos
  ```zsh
  bash MSRVTT/download_data.sh
  ```
  :hourglass: This takes about 10-30 minutes (depending on your internet connection).




### [MAD](https://github.com/Soldelli/MAD)

* Download splits and CLIP features from [official repository](https://github.com/Soldelli/MAD). It needs filling NDA and manually downloading.