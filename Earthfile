VERSION 0.6
FROM python:3
WORKDIR /code

build:
    ENV DEBIAN_FRONTEND noninteractive
    RUN apt-get update -y
    RUN apt install libgl1-mesa-glx -y
    RUN apt-get install 'ffmpeg' \
        'libsm6' \
        'libxext6' -y
    COPY localizer /code/localizer
    RUN pip install -e /code/localizer
    RUN tello --dry-run download

docker:
    FROM +build
    EXPOSE 6038/tcp
    EXPOSE 8889/tcp
    EXPOSE 9000/tcp
    EXPOSE 9617/tcp
    EXPOSE 6038/udp
    EXPOSE 8889/udp
    EXPOSE 9000/udp
    EXPOSE 9617/udp
    ENTRYPOINT ["tello"]
    SAVE IMAGE tello:latest
