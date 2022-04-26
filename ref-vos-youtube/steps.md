## Dataset

1. Download the dataset from [official website](https://youtube-vos.org/dataset/rvos/).
2. Unzip the zip file (around 470MBs)
3. Unzip folders within the zip file.
4. Download the YouTube-VOS dataset `train.zip` and `valid.zip` from their Drive. The ones provided by RVOS are incomplete.


## Environment

```bash
conda create -n rvos-cpu -y python=3.9
conda activate rvos-cpu
pip install numpy scipy pandas jupyter jupyterlab matplotlib seaborn ipdb repackage natsort gpustat joblib tqdm
conda install pytorch torchvision torchaudio cpuonly -c pytorch
# pip install torch==1.8.1+cu101 torchvision==0.9.1+cu101 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```