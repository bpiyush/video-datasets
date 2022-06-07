# Video Datasets
Common place to download, pre-process and standardise video datasets.


## Setup

Create a `conda` environment with the following packages:
```zsh
conda create -y -n base-video python=3.9
conda activate base-video
conda install -y -c conda-forge ffmpeg
pip install opencv-python av
pip install numpy pillow matplotlib pandas scipy PyYAML tqdm termcolor natsort ftfy regex ipython jupyterlab ipdb seaborn h5py

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


### [How2100M](https://www.di.ens.fr/willow/research/howto100m/)

* Download the split/metadata using:
  ```zsh
  wget https://www.rocq.inria.fr/cluster-willow/amiech/howto100m/HowTo100M.zip
  unzip HowTo100M.zip
  rm HowTo100M.zip
  ```
  :hourglass: This takes about 5-10 minutes (download size: 1.9GBs) (depending on your internet connection).
