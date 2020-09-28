#!/bin/sh

python3 -m venv .
source myenv/bin/activate
export PATH="$PATH:."
chmod 777 evt