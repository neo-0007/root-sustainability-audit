#!/usr/bin/env bash
set -e

# SETUP SCRIPT FOR UBUNTU 22, 24 AND 25
# SOURCE : https://github.com/compiler-research/ramtools/blob/develop/.github/workflows/ci.yml ( TAKEN REFERENCE FROM THIS CI PIPELINE )
# FOR MACOS USES homebrew
# https://root.cern/install/ IF YOU ARE USING ANOTHER OS USE THIS PAGE TO INSTALL root

OS="$(uname)"
ARCH="$(uname -m)"

# macOS
if [[ "$OS" == "Darwin" ]]; then
    echo "Using Homebrew to install deps..."

    if ! command -v brew &> /dev/null; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi

    brew install cmake git samtools

# Linux (Ubuntu only)
elif [[ "$OS" == "Linux" ]]; then

    if [[ ! -f /etc/os-release ]]; then
        echo "Cannot detect Linux distribution"
        exit 1
    fi

    source /etc/os-release

    if [[ "$ID" != "ubuntu" ]]; then
        echo "Only Ubuntu 22/24/25 supported"
        exit 1
    fi

    echo "Detected Ubuntu $VERSION_ID"

    sudo apt-get update
    sudo apt-get install -y \
        wget cmake build-essential git \
        libvdt-dev libtbb-dev
        samtools

    if [[ "$VERSION_ID" == "22.04" ]]; then
        ROOT_URL="https://root.cern/download/root_v6.36.00.Linux-ubuntu22.04-x86_64-gcc11.4.tar.gz"
    elif [[ "$VERSION_ID" == "24.04" ]]; then
        ROOT_URL="https://root.cern/download/root_v6.36.00.Linux-ubuntu24.04-x86_64-gcc13.3.tar.gz"
    elif [[ "$VERSION_ID" == "25.04" ]]; then
        ROOT_URL="https://root.cern/download/root_v6.36.00.Linux-ubuntu25.04-x86_64-gcc14.2.tar.gz"
    else
        echo "Unsupported Ubuntu version"
        exit 1
    fi

    echo "Downloading ROOT..."

    wget -O root.tar.gz 
    sudo tar -xzf root.tar.gz -C ./root/
    rm root.tar.gz

    echo "Activating ROOT..."
    source ./root/bin/thisroot.sh

else
    echo "Unsupported OS"
    exit 1
fi

# create a tools folder if not exist
if [[ ! -d "tools" ]]; then
    mkdir tools
fi

# Clone RAMTools
echo "Cloning RAMTools..."

if [[ -d "ramtools" ]]; then
    cd "ramtools"
    git pull
else
    git clone https://github.com/compiler-research/ramtools.git
    cd ramtools
fi

# Build RAMTools
echo "Building RAMTools..."

mkdir -p build
cd build

cmake ..
make -j$(nproc)

echo "Build finished."

echo "Moving executables to tools folder"

mv ./tools/* ./../../tools/

echo "Executables moved to tools folder"

echo "Setup complete !!"
