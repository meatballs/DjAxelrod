.. image:: https://badge.waffle.io/Axelrod-Python/DjAxelrod.svg?label=ready&title=Ready
    :target: https://waffle.io/Axelrod-Python/DjAxelrod

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/Axelrod-Python/DjAxelrod
   :target: https://gitter.im/Axelrod-Python/DjAxelrod?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

DjAxelrod
=========

A repository to reproduce Axelrod's iterated prisoner's dilemma as a Django based web application.


Installation
============

Pre-Requisites
--------------
There are four software tools which you will need on your machine for this project:

* Vagrant: https://www.vagrantup.com/downloads.html

* VirtualBox: https://www.virtualbox.org/wiki/Downloads

* Git: http://git-scm.com/downloads

* SSH: http://www.openssh.com/

Setup
-----

* Clone this repository to your machine::

    git clone --recursive https://github.com/Axelrod-Python/DjAxelrod.git
    cd djaxelrod

* Create a Virtual Machine to host the DjAxelrod application::

    cd <path to your cloned repository>
    vagrant up

This step will take some time. It has to download the operating system and all the tools to install on your new virtual machine.

* Check to see if it's working by pointing your web browser to http://localhost:8000



