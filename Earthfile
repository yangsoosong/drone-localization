VERSION 0.6
FROM python:3
WORKDIR /code
USER root

build:
    ENV DEBIAN_FRONTEND noninteractive
    RUN apt-get update --yes && \
        apt-get upgrade --yes && \
        apt-get install --yes --no-install-recommends \
        bzip2 \
        ca-certificates \
        fonts-liberation \
        locales \
        # - pandoc is used to convert notebooks to html files
        #   it's not present in arm64 ubuntu image, so we install it here
        pandoc \
        sudo \
        wget \
        git \
        tzdata \
        unzip \
        vim-tiny \
        # Inkscape is installed to be able to convert SVG files
        inkscape \
        # git-over-ssh
        openssh-client \
        # less is needed to run help in R
        # see: https://github.com/jupyter/docker-stacks/issues/1588
        less \
        # nbconvert dependencies
        # https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex
        texlive-xetex \
        texlive-fonts-recommended \
        texlive-plain-generic \
        libgl1-mesa-glx \
        ffmpeg \
        libsm6 \
        libxext6 && \
        apt-get clean
    COPY localizer /code/localizer
    RUN pip install -e /code/localizer
    RUN pip install jupyterlab
    RUN localizer --dry-run download

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
    EXPOSE 8890/tcp
    ENTRYPOINT ["/bin/bash"]
    SAVE IMAGE localizer:latest
