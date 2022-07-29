#!/bin/zsh

arch_name="$(uname -m)"

if [ "${arch_name}" = "arm64" ]; then
    echo "arm64"
else
    echo "x86_64"
fi

./install-homebrew.sh
brew update
brew install cmake
brew install boost
brew install boost-python3
brew install ffmpeg@4
brew install tcl-tk
brew install openblas

export OPENBLAS=$(/opt/homebrew/bin/brew --prefix openblas)
export CFLAGS="-falign-functions=8 ${CFLAGS}"
export PATH="/opt/homebrew/opt/ffmpeg@4/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/ffmpeg@4/lib"
export CPPFLAGS="-I/opt/homebrew/opt/ffmpeg@4/include"
export PKG_CONFIG_PATH="/opt/homebrew/opt/ffmpeg@4/lib/pkgconfig"

# ./install-pyenv.sh
# ./install-poetry.sh
./install-project.sh