FROM python:3.12-bookworm

# set variables
ARG dir=yolo_latest_runner

# update packages
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --upgrade pip

# set working dir
WORKDIR /usr/src/app

# install requirements.txt
COPY $dir/requirements.txt $dir/

RUN pip install --no-cache-dir --upgrade -r $dir/requirements.txt

# intstall yolo_runner_base
COPY yolo_runner_base yolo_runner_base

COPY pyproject.toml .

RUN pip install -e .

# install yolo8
RUN pip install ultralytics

# copy all files and set final working dir
COPY . .

WORKDIR /usr/src/app/$dir

CMD ["fastapi", "run", "main.py", "--port", "8000"]
