.. image:: https://badge.waffle.io/Axelrod-Python/DjAxelrod.svg?label=ready&title=Ready
    :target: https://waffle.io/Axelrod-Python/DjAxelrod

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/Axelrod-Python/DjAxelrod
   :target: https://gitter.im/Axelrod-Python/DjAxelrod?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

DjAxelrod
=========

A repository to extend the work in our related project, `Axelrod <https://github.com/Axelrod-Python/Axelrod>`_ by creating a Django based web application.

You can read about the background to this work at http://axelrod.readthedocs.org/en/latest/

Installation
============

Pre-Requisites
--------------
There are four software tools which you will need on your machine for this project:

* Vagrant (version 1.7.2 or later): https://www.vagrantup.com/downloads.html

* VirtualBox (version 4.3.26 or later): https://www.virtualbox.org/wiki/Downloads

* Git: http://git-scm.com/downloads

* SSH: http://www.openssh.com/

Setup
-----

* Clone this repository to your machine::

    git clone https://github.com/Axelrod-Python/DjAxelrod.git
    cd djaxelrod

* Create a Virtual Machine to host the DjAxelrod application::

    cd <path to your cloned repository>
    vagrant up

This step will take some time. It has to download the operating system and all the tools to install on your new virtual machine.

* Run Celery::

    vagrant ssh -c "cd /vagrant; celery -A djaxelrod worker -l info"


* Check to see if it's working by pointing your web browser to http://localhost:8000

Usage
=====

* Your virtual machine is running a web server which will detect any changes that you make to the project's code and show their effect immediately at http://localhost:8000.

* When you have finished working on the project, you can shut down your virtual machine using::

    vagrant halt

* And when you are ready to start work once again, bring the virtual machine back up with::

    vagrant up

  then run Celery::

    vagrant ssh -c "cd /vagrant; celery -A djaxelrod worker -l info"

* If you need to restart your virtual machine for any reason, you can use::

    vagrant reload

* You can login to your virtual machine and then administer it using::

    vagrant ssh

* You can issue a command to your virtual machine without logging into a shell. e.g. to run django migrations::

    vagrant ssh -c "cd /vagrant; python manage.py migrate"

* If you need to re-run the setup and configuration of your virtual machine, use::

    vagrant reload --provision

* And, if you break it completely and need to start again, then use::

    vagrant destroy
    vagrant up

  then run Celery::

    vagrant ssh -c "cd /vagrant; celery -A djaxelrod worker -l info"

(This will be slightly quicker than the first time as it will not need to download the operating system. It will still take some time, however).

* You can connect to the postgresql database on your virtual machine from any client on your host machine. It's running on port 8432 and the username is 'djaxelrod'. e.g.::

    psql -h locahost -p 8432 -U djaxelrod
