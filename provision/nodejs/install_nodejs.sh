#!/usr/bin/env bash
echo "*****************************"
echo "*** Installing NodeJs ***"
echo "*****************************"

apt-get -y install nodejs npm nodejs-legacy
npm install
bower install
npm install -g gulp
