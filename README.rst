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

* Clone this repository to your machine::

    $ git clone https://github.com/Axelrod-Python/DjAxelrod.git
    $ cd djaxelrod

* Recommended - Create a virtual environment for this project::

    $ <TBC>

* Install the required python libraries::

    $ pip install -r requirements.txt

* Create a database

* Define your local environment::

    $ mv .env.sample .env

Enter the details for your database in the 'DATABASE_URL' key within the .env file

* Generate a secret key::

    $ python -c 'import random; import string; print "".join([random.SystemRandom().choice(string.digits + string.letters + string.punctuation) for i in range(100)])'

Paste the output into the 'SECRET_KEY' key within the .env file


