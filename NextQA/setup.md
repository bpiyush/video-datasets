# [NextQA Dataset]()

* Download set of training and validation video zips from [VIDOR page](https://xdshang.github.io/docs/vidor.html). I had to do this manually since `wget` didn't work for me.
* Move to a central location
```sh
data_root=/Users/piyush/datasets/
cd $data_root
mkdir next-qa
cd next-qa
mkdir zips

# move the downloaded zips to this folder
mv /path/to/downloads/training-video-part*.zip $data_root/next-qa/zips/
mv /path/to/downloads/validation-video.zip $data_root/next-qa/zips/
mv /path/to/downloads/test-data-nextqa.zip $data_root/next-qa/zips 

# and unzip them
unzip zips/training-video-part*.zip -d $data_root/next-qa/
unzip zips/validation-video.zip -d $data_root/next-qa/
unzip zips/test-data-nextqa.zip -d $data_root/next-qa/

# delete the zips
rm -rf $data_root/next-qa/zips/*.zip
```
* Download mapping from VIDOR to NextQA 
```sh
gdown --id 1NFAOQYZ-D0LOpcny8fm0fSzLvN0tNR2A
du -sh map_vid_vidorID.json
```
* Download open-ended questions
```sh
gdown --id 1wOhytywctSY0WV18g5v4OttyX1TEY8j9
unzip nextqa.zip
rm nextqa.zip
```
* Download test set for NextQA from the [official homepage](https://doc-doc.github.io/docs/nextqa.html).
