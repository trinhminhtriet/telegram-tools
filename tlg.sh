#!/bin/bash

EXEC_TIME=`date +"%Y-%m-%d %H:%M:%S"`
echo "$EXEC_TIME"

cd /data/trinhminhtriet/telegram-tools

# python3 -m venv ./.venv
. ./.venv/bin/activate
# pip install -r requirements.txt 
python --version

python app.py