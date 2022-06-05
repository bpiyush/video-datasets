# read arguments from the user
while getopts ":d:h" opt; do
  case $opt in
    d)
      data_root=$OPTARG
      ;;
    h)
      echo "Usage: download_data.sh -d <dataset path>"
      echo "  -d <data_root>  : dataset path to download to"
      exit 0
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

# set root data folder: set default
if [ -z "$data_root" ]; then
  data_root=/ssd/pbagad/datasets/MSR-VTT/
fi
echo ">>> Downloading MSR-VTT dataset to $data_root"
exit
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
