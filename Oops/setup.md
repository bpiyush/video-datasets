* Download the dataset
```sh
data_root=/var/scratch/pbagad/datasets/oops
mkdir -p $data_root

cd $data_root
# download videos
wget https://oops.cs.columbia.edu/data/video_and_anns.tar.gz
tar -xvf video_and_anns.tar.gz
rm -rf video_and_anns.tar.gz
cd oops_dataset
tar -xvf videos.tar.gz
rm -rf videos.tar.gz
tar -xvf annotations.tar.gz
rm -rf annotations.tar.gz video.tar.gz

# download language descriptions
wget https://oops.cs.columbia.edu/data/lang.tar.gz
tar vxf lang.tar.gz
rm lang.tar.gz
```