FROM python:3.12-bookworm

# set variables
ARG dir=yolo_latest_runner

# update packages
RUN apt-get update && apt-get upgrade -y

RUN apt-get install \
    ffmpeg libsm6 libxext6  -y

RUN pip install --upgrade pip

# set working dir
WORKDIR /usr/src/app

# install requirements_common.txt
COPY requirements_common.txt .

RUN pip install --no-cache-dir -r requirements_common.txt

# intstall yolo_runner_base
COPY yolo_runner_base yolo_runner_base

COPY pyproject.toml .

RUN pip install --no-cache-dir -e .

# install ultralytics
RUN pip install --no-cache-dir ultralytics

# copy yolo_runner files and set final working dir
COPY $dir $dir

WORKDIR /usr/src/app/$dir

CMD ["fastapi", "run", "main.py", "--port", "8000"]
