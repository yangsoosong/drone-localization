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
brew install ffmpeg
brew install tcl-tk
./install-pyenv.sh
./install-poetry.sh
./install-project.sh