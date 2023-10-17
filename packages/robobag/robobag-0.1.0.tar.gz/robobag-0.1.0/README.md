# robobag

Profile rosbag file and extract structured/unstructed topic data to parquet/mp4/jpeg/json/jsonl .

## env

```bash
conda create -n robobag python=3.10
conda activate robobag
pip install -r requirements.txt

brew install protobuf
protoc -I=./ --python_out=./robobag ./profile.proto
```

## install

```bash
# build package and publish
python3 setup.py sdist
pip install twine
twine upload dist/*

# install from local
pip3 install dist/robobag-1.0.0.tar.gz

```

## use

```bash
robobag --help
robobag profile -i /path/to/data.bag
robobag extract -i /path/to/data.bag -t /topic -f parquet
robobag extract -i /path/to/data.bag -t /topic -f mp4
robobag extract -i /path/to/data.bag -t /topic -f jpeg_seq
robobag extract -i /path/to/data.bag -t /topic -f json
robobag extract -i /path/to/data.bag -t /topic -f jsonl
```

![profile web](web.png)

### test

```bash
python3 -m robobag.cli profile -i /path/to/data.bag
python3 -m robobag.cli extract -i /path/to/data.bag -t /topic -f parquet
```
