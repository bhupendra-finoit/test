Solvecore
=========

# Important Notes

This guide is long because it covers many cases and includes all commands you need.

This installation guide was created for and tested on **Ubuntu 16.04** operating systems.

This is the official installation guide to set up a production server. To set up a **development installation** and to contribute read `Contributing.md`.

The following steps have been known to work. Please **use caution when you deviate** from this guide. Make sure you don't violate any assumptions Solvecore makes about its environment.

# Overview

The  Solvecore installation consists of setting up the following components:

1. Packages / Dependencies
1. System Users
1. Database
1. Solvecore
1. Supervisor
1. Nginx
1. Update Existing Setup to Newer Version

## Packages / Dependencies

Run following commands

    sudo apt-get update
    sudo apt-get -y upgrade

**Note:** During this installation some files will need to be edited manually. If you are familiar with vim set it as default editor with the commands below. If you are not familiar with vim please skip this and keep using the default editor.

    # Install vim and set as default editor
    sudo apt-get install -y vim-gnome
    sudo update-alternatives --set editor /usr/bin/vim.gnome

Install the required packages (needed to compile Ruby and native extensions to Ruby gems):

    sudo apt-get install -y build-essential git-core libssl-dev libffi-dev curl redis-server checkinstall libcurl4-openssl-dev python-docutils pkg-config python3-dev python-dev python-virtualenv

**Note:** In order to receive mail notifications, make sure to install a mail server. The recommended mail server is postfix and you can install it with:

    sudo apt-get install -y postfix

Then select 'Internet Site' and press enter to confirm the hostname.

# System Users

Create a `solvecore` user for Solvecore:

    sudo adduser --disabled-login --gecos 'Solvecore' solvecore

# Database

We recommend using a PostgreSQL database.

    # Install the database packages
    sudo apt-get install -y postgresql postgresql-client libpq-dev

    # Login to PostgreSQL
    sudo -u postgres psql -d postgres

    # Create a user for Solvecore
    # Do not type the 'postgres=#', this is part of the prompt
    postgres=# CREATE USER solvecore WITH PASSWORD '123456' CREATEDB;

    # Create the Solvecore production database & grant all privileges on database
    postgres=# CREATE DATABASE solvecore_production OWNER solvecore;

    # Quit the database session
    postgres=# \q

    # Try connecting to the new database with the new user
    sudo -u solvecore -H psql -d solvecore_production

    # Quit the database session
    solvecore_production> \q

# Solvecore

    # We'll install Solvecore into home directory of the user "solvecore"
    cd /home/solvecore

## Clone the Source

    # Clone Solvecore repository
    sudo -u solvecore -H solvecore clone https://github.com/solvecore/solvecore.git solvecore

## Configure It

    # Switch User solvecore
    sudo su solvecore

    # Go to Solvecore installation folder
    cd /home/solvecore/solvecore

    # Virtual Envirnoment and requirements
    virtualenv -p /usr/bin/python3.4 env
    source env/bin/activate
    pip install -r requirements.txt

## Project and Database Configuartion Settings

    # Edit desired configurations in config/local.py i.e. STATICFILES_DIRS
    cp config/local.py.example config/local.py
    chmod o-rwx config/local.py
    editor config/local.py

Example:

        DEBUG = False

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'solvecore_production',
                'USER': 'solvecore',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': '',
            }
        }

## Validate configurations

    ./manage.py check

## Migrate Database & Seed Default Data

    ./manage.py migrate
    ./manage.py loaddata fixtures/default.json

## Load Assets

    ./manage.py collectstatic

## Gunicorn Or uWSGI

    # Copy either of the configuration file for respective server
    cp scripts/gunicorn.bash scripts/runserver.bash

    OR

    cp scripts/uwsgi.bash scripts/runserver.bash

    # Make it executable
    chmod u+x scripts/runserver.bash

## Exit User solvecore

    exit

# Supervisor

## Installation

    sudo apt-get install -y supervisor

    # Go to Solvecore installation folder
    cd /home/solvecore/solvecore

## Configuration

    sudo cp config/supervisor/solvecore.conf /etc/supervisor/conf.d/solvecore.conf
    sudo cp config/supervisor/solvecore_celery.conf /etc/supervisor/conf.d/solvecore_celery.conf
    sudo cp config/supervisor/solvecore_celerybeat.conf /etc/supervisor/conf.d/solvecore_celerybeat.conf

## Supervisor Configuration Update

    sudo service supervisor restart
    sudo supervisorctl reread
    sudo supervisorctl update

# Nginx

## Installation

    sudo apt-get install -y nginx

## Site Configuration

    # Copy the example site config:
    sudo cp config/nginx/solvecore /etc/nginx/sites-available/solvecore
    sudo ln -s /etc/nginx/sites-available/solvecore /etc/nginx/sites-enabled/solvecore

Make sure to edit the config file to match your setup:

    # Change YOUR_SERVER_FQDN to the fully-qualified
    # domain name of your host serving Solvecore.
    sudo editor /etc/nginx/sites-available/solvecore

**Note:** If you want to use HTTPS, replace the `solvecore` Nginx config with `solvecore-ssl`. See [Using HTTPS](#using-https) for HTTPS configuration details.

## Test Configuration

Validate your `solvecore` or `solvecore-ssl` Nginx config file with the following command:

    sudo nginx -t

You should receive `syntax is okay` and `test is successful` messages. If you receive errors check your `solvecore` or `solvecore-ssl` Nginx config file for typos, etc. as indicated in the error message given.

## Provide access to static files and error templates

    sudo adduser nginx solvecore
    sudo chmod -R 750 /home/solvecore/solvecore/static/
    sudo chmod -R 750 /home/solvecore/solvecore/templates/

## Restart

    sudo service nginx restart

# Update Existing Setup to Newer Version


# Using HTTPS

To use Solvecore with HTTPS:


Using a self-signed certificate is discouraged but if you must use it follow the normal directions then:

1. Generate a self-signed SSL certificate:

    ```
    mkdir -p /etc/nginx/ssl/
    cd /etc/nginx/ssl/
    sudo openssl req -newkey rsa:2048 -x509 -nodes -days 3560 -out solvecore.crt -keyout solvecore.key
    sudo chmod o-r solvecore.key
    ```
