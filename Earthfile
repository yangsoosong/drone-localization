VERSION 0.6
FROM python:3
WORKDIR /code

build:
    ENV DEBIAN_FRONTEND noninteractive
    RUN apt-get update -y
    RUN apt-get install 'libgl1-mesa-glx' \
        'ffmpeg' \
        'libsm6' \
        'libxext6' \
        'libqt5gui5' \
        'libqt5x11extras5' \
        'freeglut3-dev' \
        'libsm6' \
        'libdbus-1-3' \
        'libxkbcommon-x11-0' \
        'libxcb-icccm4' \
        'libxcb-image0' \
        'libxcb-keysyms1' \
        'libxcb-randr0' \
        'libxcb-render-util0' \
        'libxcb-xinerama0' \
        'libxcb-xinput0' \
        'libxcb-xfixes0' -y
    RUN rm -rf /var/lib/apt/lists/*
    ENV QT_DEBUG_PLUGINS=1

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
