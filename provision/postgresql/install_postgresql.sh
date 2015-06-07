#!/usr/bin/env bash
echo "*****************************"
echo "*** Installing Postgresql ***"
echo "*****************************"

PG_VERSION=9.3

# Install the packages
apt-get -y install postgresql postgresql-contrib

# Sort out remote connections from host
sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/$PG_VERSION/main/postgresql.conf
echo "host    all             all             0.0.0.0/0               md5" | sudo tee -a /etc/postgresql/$PG_VERSION/main/pg_hba.conf

# Create the 'vagrant' db user
user_exists=`sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='vagrant'"`
if [[ $user_exists != "1" ]]
then
    su postgres -c "createuser -s vagrant"
    sudo -u postgres psql -c "CREATE ROLE root LOGIN NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;"
fi

# Restart the service so the changes take effect
sudo service postgresql restart
