#!/bin/zsh

arch_name="$(uname -m)"

if [ "${arch_name}" = "arm64" ]; then
    echo "M1 Mac"
    brew update
    brew install cmake
    brew install boost
    brew install boost-python3
    brew install ffmpeg
    brew install tcl-tk
else
    echo "Fedora"
    dnf install cmake
    dnf install boost
    dnf install boost-python3
    dnf install ffmpeg
    dnf install tcl-tk
fi
