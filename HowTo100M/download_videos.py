"""Downloads given list of videos from HowTo100M dataset."""
import os
from typing import Iterator
import requests
import pandas as pd
import numpy as np
import time
from tqdm import tqdm
from joblib import Parallel, delayed
import torch

from utils.io import load_json, save_json

import warnings
warnings.filterwarnings("ignore")


# enter your credentials
USER_ID = ""
PASSWORD = ""

assert USER_ID != "", "Please enter your USER_ID first."
assert PASSWORD != "", "Please enter your PASSWORD first."


def download_video(url, path):
    response = requests.get(url, auth=requests.auth.HTTPBasicAuth(USER_ID, PASSWORD))
    
    # save video
    with open(path, "wb") as f:
        f.write(response.content)


def check_and_download(url, path):
    if not os.path.exists(path):
        try:
            download_video(url, path)
            return True
        except:
            return False


def download_videos(ids, urls, output_dir, debug=False, debug_num=100):
    """Downloads given bunch of videos."""
    
    if debug:
        urls = urls[:debug_num]
        ids = ids[:debug_num]
    
    # download_report = dict()

    # make the directory
    os.makedirs(output_dir, exist_ok=True)
    
    # configure paths
    paths = list(map(lambda x: os.path.join(output_dir, x + ".mp4"), ids))
    
    exists = list(map(os.path.exists, paths))
    
    download_ids = np.array(ids)[~np.array(exists)]
    download_urls = np.array(urls)[~np.array(exists)]
    download_paths = np.array(paths)[~np.array(exists)]
    
    exist_ids = np.array(ids)[np.array(exists)]
    
    if len(download_ids):
        iterator = tqdm(zip(download_urls, download_paths), total=len(download_urls), desc="Downloading")
        outputs = Parallel(n_jobs=8)(delayed(check_and_download)(url, path) for url, path in iterator)

        success_ids = np.array(download_ids)[np.array(outputs)]
        failure_ids = np.array(download_ids)[~np.array(outputs)]
    else:
        success_ids = []
        failure_ids = []
    
    assert len(success_ids) + len(failure_ids) == len(download_ids)
    assert len(download_ids) + len(exist_ids) == len(ids)
    
    report = dict(
        ids=ids,
        exist_ids=exist_ids,
        success_ids=success_ids,
        failure_ids=failure_ids,
    )
    
    return report



if __name__ == "__main__":
    data_root = "/var/scratch/pbagad/datasets"
    data_dir = os.path.join(data_root, "howto100m")
    split_dir = os.path.join(data_dir, "subsets")
    
    print(">>> Loading split...")
    original_metadata = pd.read_csv(os.path.join(data_dir, "HowTo100M_v1.csv"))
    meta_path = os.path.join(split_dir, "HowTo100M_v1-v1.0_100k.csv")
    metadata = pd.read_csv(meta_path)
    print()
    
    print(">>> Loading annotations...")
    anno_path = os.path.join(split_dir, "captions-v1.0_100k.json")
    start = time.time()
    annodata = load_json(anno_path)
    end = time.time()
    print(">>> Time taken to load annotations: {:.2f} seconds".format(end - start))
    print()
    
    url_file = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "download_instructions/howto100m_videos.txt",
    )
    assert os.path.exists(url_file), "URL file does not exist at {}".format(url_file)
    urls = np.loadtxt(url_file, dtype=str)
    # urls = set(urls)
    
    required_urls = [f"http://howto100m.inria.fr/dataset/{v}.mp4" for v in metadata.video_id]
    
    url_to_id = map(lambda x: os.path.basename(x).split(".")[0], urls)
    ids = list(url_to_id)
    df = pd.DataFrame({"video_id": ids, "url": urls})
    subdf = df[df.video_id.isin(set(metadata.video_id))]
    subdf["url"] = subdf["url"].apply(lambda x: x.replace("http", "https"))
    
    save_path = os.path.join(data_dir, "subsets", "id_to_url-v1.0_100k.csv")
    subdf.to_csv(save_path, index=False)
    
    video_dir = os.path.join(data_dir, "videos")
    os.makedirs(video_dir, exist_ok=True)

    download_sample = False
    if download_sample:
        sample_id, sample_url = subdf.iloc[0]
        print(">>> Downloading sample video {}...".format(sample_id))
        sample_path = os.path.join(data_dir, "videos", sample_id + ".mp4")
        start = time.time()
        download_video(sample_url, sample_path)
        end = time.time()
        print(">>> Time taken to download video: {:.2f} seconds".format(end - start))
    
    # download
    start = time.time()
    report = download_videos(subdf.video_id, subdf.url, video_dir, debug=False)
    end = time.time()
    print(">>> Finished downloading videos in {:.2f} seconds".format(end - start))
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    report_path = os.path.join(data_dir, "subsets", "download_report-v1.0_100k-{}.pt".format(timestamp))
    torch.save(report, report_path)
    