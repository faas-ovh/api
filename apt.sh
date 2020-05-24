#!/bin/bash
ps aux | grep -i apt
#killall apt
#pkill apt
pkill apt-get
sudo dpkg --configure -a
