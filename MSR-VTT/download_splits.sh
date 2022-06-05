# set root data folder
data_root=/ssd/pbagad/datasets/MSR-VTT/
mkdir -p $data_root

# download splits
# Ref: https://github.com/ArrowLuo/CLIP4Clip
cd $data_root
echo "Downloading MSR-VTT splits..."
wget https://github.com/ArrowLuo/CLIP4Clip/releases/download/v0.0/msrvtt_data.zip
unzip msrvtt_data.zip
rm -rf msrvtt_data.zip
echo "Downloaded splits for MSR-VTT"
ls -l $data_root/msrvtt_data/

# download raw videos
echo "Downloading MSR-VTT raw videos..."
# Ref 1: https://github.com/ArrowLuo/CLIP4Clip
# Ref 2: https://github.com/m-bain/frozen-in-time#-finetuning-benchmarks-msr-vtt
wget https://www.robots.ox.ac.uk/~maxbain/frozen-in-time/data/MSRVTT.zip
unzip MSRVTT.zip
rm -rf MSRVTT.zip
echo "Downloaded raw videos for MSR-VTT"
ls -l $data_root/MSRVTT/
