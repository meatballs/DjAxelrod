#!/usr/bin/env bash
echo "*****************************"
echo "*** Installing NodeJs ***"
echo "*****************************"

apt-get -y install nodejs npm nodejs-legacy
npm install
npm install -g bower
su -c "bower install -s" vagrant
npm install -g gulp

# configure Gulp as an upstart daemon
cp /vagrant/provision/nodejs/gulp-server.conf /etc/init
if (( $(ps -ef | grep -v grep | grep "gulp" | wc -l) > 0 ))
then
    restart gulp-server
else
    start gulp-server
fi
