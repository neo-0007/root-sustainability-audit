#!/usr/bin/env bash
set -e

# SETUP SCRIPT FOR UBUNTU 22, 24 AND 25
# SOURCE : https://github.com/compiler-research/ramtools/blob/develop/.github/workflows/ci.yml ( TAKEN REFERENCE FROM THIS CI PIPELINE )
# FOR MACOS USES homebrew
# https://root.cern/install/ IF YOU ARE USING ANOTHER OS USE THIS PAGE TO INSTALL root

OS="$(uname)"
ARCH="$(uname -m)"
INSTALL_DIR="$HOME/ramtools"

# macOS
if [[ "$OS" == "Darwin" ]]; then
    echo "Using Homebrew to install ROOT..."

    if ! command -v brew &> /dev/null; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi

    brew install root cmake git

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

    ROOT_URL=""

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

    wget -O root.tar.gz $ROOT_URL
    sudo mkdir -p /opt/root
    sudo tar -xzf root.tar.gz -C /opt/
    rm root.tar.gz

    echo "Activating ROOT..."
    source /opt/root/bin/thisroot.sh

else
    echo "Unsupported OS"
    exit 1
fi

# Clone RAMTools
echo "Cloning RAMTools..."

if [[ -d "$INSTALL_DIR" ]]; then
    cd "$INSTALL_DIR"
    git pull
else
    git clone https://github.com/compiler-research/ramtools.git "$INSTALL_DIR"
    cd "$INSTALL_DIR"
fi

# Build RAMTools
echo "Building RAMTools..."

mkdir -p build
cd build

cmake ..
make -j$(nproc 2>/dev/null || sysctl -n hw.ncpu)

echo "Build finished."
