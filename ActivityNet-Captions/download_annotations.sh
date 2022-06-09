# Downloads ActivityNet Captions from official website

# set root data folder
data_root=/ssd/pbagad/datasets/activitynet-1.3/annotations
mkdir -p $data_root

# download zip files
cd $data_root

# check if the folder does not already exist
if [ ! -d "captions" ]; then
    wget https://cs.stanford.edu/people/ranjaykrishna/densevid/captions.zip
    unzip captions.zip
    rm captions.zip
else
    echo "Captions already downloaded at $data_root/captions"
fi