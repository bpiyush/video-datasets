* Download the `README`
```sh
cd HowTo100M

url=https://www.rocq.inria.fr/cluster-willow/amiech/howto100m/download_instructions.zip
wget $url
unzip download_instructions.zip
rm -rf download_instructions.zip
```
* Set data root
```sh
data_root=/var/scratch/pbagad/datasets/howto100m/
mkdir -p $data_root
```
* Download annotations
```sh
url=https://www.rocq.inria.fr/cluster-willow/amiech/howto100m/HowTo100M.zip
wget $url -O $data_root/HowTo100M.zip
unzip $data_root/HowTo100M.zip -d $data_root
rm -rf $data_root/HowTo100M.zip
```
* Generate S3D features (based on `fairseq/examples/MMPT` repo from FAIR (see my repo `Test-of-Time-dev/external` for this.
```sh
cd external/fairseq/examples/MMPT/
vdir=/var/scratch/pbagad/datasets/howto100m/videos/
fdir=/var/scratch/pbagad/datasets/howto100m/feat/feat_how2_s3d/
mkdir -p $fdir
python scripts/video_feature_extractor/extract.py --vdir $vdir --fdir $fdir --type=s3d --num_decoding_thread=4 --batch_size 32 --half_precision 1
```
