#!/bin/bash

# Install veraPDF on a Linux system

# USAGE: ./install-verapdf.sh

set -o pipefail -o errexit -o nounset -o xtrace

wget --quiet http://downloads.verapdf.org/rel/verapdf-installer.zip
unzip verapdf-installer.zip
rm verapdf-installer.zip
cd verapdf-*
echo 1 | ./verapdf-install
