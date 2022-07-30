arch_name="$(uname -m)"

docker pull ghcr.io/itsjohnward/localizer:latest_linux_${arch_name} && \
docker run --rm -it \
   --ipc=host \
   --volume `pwd`:/code \
   -p 0.0.0.0:6038:6038/udp \
   -p 0.0.0.0:8889:8889/udp \
   -p 0.0.0.0:9000:9000/udp \
   -p 0.0.0.0:9617:9617/udp \
   -p 0.0.0.0:6038:6038/tcp \
   -p 0.0.0.0:8889:8889/tcp \
   -p 0.0.0.0:9000:9000/tcp \
   -p 0.0.0.0:9617:9617/tcp \
   -p 0.0.0.0:8890:8890/tcp \
   ghcr.io/itsjohnward/localizer:latest_linux_${arch_name} -c "jupyter lab --allow-root --ip=0.0.0.0 --port=8890"