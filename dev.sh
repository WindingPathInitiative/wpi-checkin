#!/bin/bash
cd "$(dirname "$0")"
. venv/bin/activate
FLASK_APP=checkin.py flask run