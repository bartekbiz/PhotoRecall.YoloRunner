FROM python:3.12-bookworm

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN pip install ultralytics

COPY . .

CMD ["fastapi", "run", "main.py", "--port", "8000"]
