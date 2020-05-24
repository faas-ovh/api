#!/bin/bash
#command -v git >/dev/null 2>&1 || { echo >&2 "I require git but it's not installed.  Aborting."; exit 1; }
apt-get update -y
apt-get install git -y
git --version
git clone git://github.com/promagen/debian.git promagen-debian
cd promagen-debian
sh download.sh
sh install.sh
sh start.sh
