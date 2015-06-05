#!/usr/bin/env bash
echo "*****************************"
echo "*** Installing NodeJs ***"
echo "*****************************"

apt-get -y install nodejs npm nodejs-legacy
npm install
npm install -g bower
bower install -s
npm install -g gulp
