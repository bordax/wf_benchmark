#!/bin/sh
#gunicorn --bind 0.0.0.0:8000 main:app -w4 --worker-class uvicorn.workers.UvicornWorker
uvicorn --host 0.0.0.0 --port 8000 main:app