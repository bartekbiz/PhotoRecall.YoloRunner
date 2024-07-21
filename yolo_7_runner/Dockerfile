FROM python:3.10-bookworm

# set variables
ARG dir=yolo_7_runner

# update packages
RUN apt-get update && apt-get upgrade -y

RUN apt-get install \
    ffmpeg libsm6 libxext6 zip htop screen libgl1-mesa-glx -y

RUN pip install --upgrade pip

# set working dir
WORKDIR /usr/src/app

# install requirements_common.txt
COPY requirements_common.txt .

RUN pip install --no-cache-dir -r requirements_common.txt

# install yolov7
ARG yolo_dir=$dir/yolov7

RUN mkdir -p $yolo_dir

RUN git clone https://github.com/WongKinYiu/yolov7.git $yolo_dir

RUN pip install --no-cache-dir -r $yolo_dir/requirements.txt

# intstall yolo_runner_base
COPY yolo_runner_base yolo_runner_base

COPY pyproject.toml .

RUN pip install --no-cache-dir -e .

# copy yolo_runner files and set final working dir
COPY $dir $dir

WORKDIR /usr/src/app/$dir

CMD ["fastapi", "run", "main.py", "--port", "8000"]
