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