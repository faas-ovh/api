#apt update
command -v git >/dev/null 2>&1 || { echo >&2 "I require git but it's not installed.  Aborting."; exit 1; }
#git clone git@github.com:promagen/debian.git promagen-debian
#git clone https://github.com/promagen/debian.git promagen-debian
#git clone git@github.com:promagen/debian.git promagen-debian
git clone git://github.com/promagen/debian.git promagen-debian
cd promagen-debian
sh download.sh
