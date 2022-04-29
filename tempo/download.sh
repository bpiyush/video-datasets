DATA_DIR=/ssd/pbagad/datasets/TEMPO/
mkdir -p $DATA_DIR

cd $DATA_DIR
wget https://data.ciirc.cvut.cz/public/projects/LisaAnne/TEMPO/initial_release_data.zip
unzip initial_release_data.zip
cd -

echo "Downloaded TEMPO data files to $DATA_DIR/initial_release_data/"