#! /bin/sh

pip install gunicorn flask
gunicorn -w4 -b :8000 main:app
