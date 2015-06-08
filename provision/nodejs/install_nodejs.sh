#!/usr/bin/env bash
echo "*****************************"
echo "*** Installing NodeJs ***"
echo "*****************************"

apt-get -y install nodejs npm nodejs-legacy
npm install
npm install -g bower
su -c "bower install -S" vagrant
npm install -g gulp
