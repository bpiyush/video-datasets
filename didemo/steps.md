
The data files have been copied from Lisa Anne Hendrick's [GitHub repository](https://github.com/LisaAnne/LocalizingMoments).

Download videos from AWS:
```bash
cd didemo
DATA_DIR=/ssd/pbagad/datasets/DiDeMo/videos/
mkdir -p $DATA_DIR
python download_videos_AWS.py --video_directory $DATA_DIR --download
```

Download (13) missing videos:
```bash
# this will create missing_videos.txt in $DATA_DIR/../
python download_videos_AWS.py --video_directory $DATA_DIR
```
Further, you can download and unzip missing videos from [this Drive link](https://drive.google.com/drive/u/0/folders/1heYHAOJX0mdeLH95jxdfxry6RC_KMVyZ) provided by the authors.

Add these videos to the same `$DATA_DIR`.