#!/usr/bin/env bash
echo "Starting initial Vagrant provision"

locale="en_GB.UTF-8"
timezone="Europe/London"

/usr/sbin/locale-gen $locale
/usr/sbin/update-locale LANG=$locale LC_ALL=$locale
echo $timezone > /etc/timezone
dpkg-reconfigure -f noninteractive tzdata
apt-get update
apt-get install -y git curl pkg-config
