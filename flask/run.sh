#!/bin/sh
#gunicorn --bind 0.0.0.0:5000 -w4 main:app
export FLASK_APP=main
flask run --host 0.0.0.0