FROM python:3.10

EXPOSE 6038/tcp
EXPOSE 8889/tcp
EXPOSE 9000/tcp
EXPOSE 9617/tcp
EXPOSE 6038/udp
EXPOSE 8889/udp
EXPOSE 9000/udp
EXPOSE 9617/udp

RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg' \
'libsm6' \
'libxext6' -y

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN --mount=type=ssh pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

ENV PYTHONPATH /usr/src/app
CMD tail -f /dev/null
