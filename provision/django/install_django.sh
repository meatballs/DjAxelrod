#!/usr/bin/env bash
echo "*************************"
echo "*** Installing Django ***"
echo "*************************"

if [[ -z "$1" ]]
then
  echo "Django project name not set. Check the Vagrant file."
  exit 1
else
  DJANGO_PROJECT=$1
fi

# install pip
apt-get install -y python-pip

# install packages for python-postgresql connectivity
apt-get install -y libpq-dev python-dev

# install python packages
pip install -r /vagrant/requirements.txt

# Set environment variables
sudo echo "DEBUG=TRUE" >> /etc/environment
sudo echo "SECRET_KEY='LousyKeyOnlySuitableForDevEnvironments'" >> /etc/environment
sudo echo "DATABASE_URL='postgres://$DJANGO_PROJECT:$DJANGO_PROJECT@localhost/$DJANGO_PROJECT'" >> /etc/environment
. /etc/environment
export DATABASE_URL
export DEBUG
export SECRET_KEY

# Create database
su postgres -c "createuser -w -d -r -s $DJANGO_PROJECT"
sudo -u postgres psql -c "ALTER USER $DJANGO_PROJECT WITH PASSWORD '$DJANGO_PROJECT';"
su postgres -c "createdb -O $DJANGO_PROJECT $DJANGO_PROJECT"
cd /vagrant
python manage.py migrate

# configure the django dev server as an upstart daemon
cp /vagrant/provision/django/django-server.conf /etc/init
start django-server
