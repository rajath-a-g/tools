#!/bin/bash

python3 -m venv myenv && \
source myenv/bin/activate && \
export PATH="$PATH:." && \
chmod 777 evt && \
python3 -m pip install gitpython
