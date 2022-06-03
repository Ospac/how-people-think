#!/bin/bash
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y python3
sudo apt-get install -y python-pip
sudo apt-get install -y zip
sudo apt-get install -y unzip

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt 

PATH_NAME=$(pwd)

cd /tmp

PATH_NAME2=$(pwd)

echo "moved to ${PATH_NAME2}"
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install --fix-broken -y
sudo dpkg -i google-chrome-stable_current_amd64.deb

cd ${PATH_NAME}
echo "moved to ${PATH_NAME}"

echo "Please enter the Password"
read p
while :
do
	unzip -P ${p} env.zip
	if [ $? -eq 0 ]; then
		echo "You entered correct password!"
		break
	else
		echo "You entered incorrect password!"
	fi
done

echo "Done."
echo ""
google-chrome --version
echo "Make sure the current version is 102. If not, please manually download later version of chromedriver."
