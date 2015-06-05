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
apt-get install python-setuptools
easy_install pip

# install packages for python-postgresql connectivity
apt-get install -y libpq-dev python-dev

# install python packages
pip install -r /vagrant/requirements.txt
pip install django-debug-toolbar

# Set environment variables
sudo echo "DEBUG=TRUE" >> /etc/environment
sudo echo "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='237400346062-fgmcf2r36vgqfh0nuisd8ofi8ot5nrp4.apps.googleusercontent.com'" >> /etc/environment
sudo echo "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='sKyWX8OQnuIWusn3WTFEevQt'" >> /etc/environment
sudo echo "SECRET_KEY='LousyKeyOnlySuitableForDevEnvironments'" >> /etc/environment
sudo echo "DATABASE_URL='postgres://$DJANGO_PROJECT:$DJANGO_PROJECT@localhost/$DJANGO_PROJECT'" >> /etc/environment
. /etc/environment
export DATABASE_URL
export DEBUG
export SECRET_KEY

# Create database
user_exists=`sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='$DJANGO_PROJECT'"`
db_exists=`sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='$DJANGO_PROJECT'"`

if [[ $user_exists != "1" ]]
then
    su postgres -c "createuser -w -d -r -s $DJANGO_PROJECT"
fi

sudo -u postgres psql -c "ALTER USER $DJANGO_PROJECT WITH PASSWORD '$DJANGO_PROJECT';"

if [[ $db_exists != "1" ]]
then
    su postgres -c "createdb -O $DJANGO_PROJECT $DJANGO_PROJECT"
fi

cd /vagrant
python manage.py migrate

# configure the django dev server as an upstart daemon
cp /vagrant/provision/django/django-server.conf /etc/init
restart django-server
