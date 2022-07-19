VERSION 0.6
FROM python:3
WORKDIR /code

install:
    ENV DEBIAN_FRONTEND noninteractive
    RUN apt-get update -y
    RUN apt install libgl1-mesa-glx -y
    RUN apt-get install 'ffmpeg' \
        'libsm6' \
        'libxext6' -y
    COPY localizer /code/localizer
    RUN pip install -e /code/localizer
    ENTRYPOINT ["tello"]
    SAVE IMAGE python-example:latest
