#!/bin/bash
deactivate > /dev/null || true
python3 -m venv myenv && \
source myenv/bin/activate && \
export PATH="$PATH:." && \
chmod 775 evt && \
python3 -m pip -q install gitpython
