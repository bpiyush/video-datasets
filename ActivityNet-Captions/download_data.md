Paper: [Dense-Captioning Events in Videos](https://arxiv.org/pdf/1705.00754.pdf)

* Download annotations
```sh
wget http://ec2-52-25-205-214.us-west-2.compute.amazonaws.com/files/activity_net.v1-3.min.json
wget https://raw.githubusercontent.com/activitynet/ActivityNet/master/Crawler/run_crosscheck.py
```
* Download requirements
```sh
pip install youtube_dl
```
* Download downloader script
```sh
wget https://raw.githubusercontent.com/activitynet/ActivityNet/master/Crawler/fetch_activitynet_videos.sh
```
* Download
```sh
VIDEO_PATH=/path/to/storage/
mkdir -p $VIDEO_PATH
chmod +x fetch_activitynet_videos.sh
```
