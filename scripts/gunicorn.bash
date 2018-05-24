#!/bin/bash

# Name of the application
NAME="solvecore"

# Django project directory
DJANGODIR=/home/solvecore/solvecore

# The user to run as
USER=solvecore

# The group to run as
GROUP=solvecore

# How many worker processes should Gunicorn spawn
NUM_WORKERS=3

# Number of seconds (Default 30 seconds)
TIMEOUT=60

# Which settings file should Django use
DJANGO_SETTINGS_MODULE=config.settings

# WSGI module name
DJANGO_WSGI_MODULE=config.wsgi

# Access logs
ACCESS_LOG='/home/solvecore/solvecore/tmp/logs/access.log'

# Error logs
ERROR_LOG='/home/solvecore/solvecore/tmp/logs/error.log'

# Log Level
LOG_LEVEL=debug # Options are debug, info, warning, error, critical

# Socket File to bind to
SOCKFILE=/home/solvecore/solvecore/tmp/sockets/gunicorn.sock

################################# END OF CONFIGURATIONS #################################


# ---------------------------------------------------------------------------------------

# Change to project directory
cd $DJANGODIR

# Activate the virtual environment
source env/bin/activate

# Activate project environment
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn $DJANGO_WSGI_MODULE:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --timeout $TIMEOUT \
  --user=$USER --group=$GROUP \
  --log-level=$LOG_LEVEL \
  --bind=unix:$SOCKFILE \
#  --bind=localhost:9090 \
  --access-logfile $ACCESS_LOG \
  --error-logfile $ERROR_LOG
