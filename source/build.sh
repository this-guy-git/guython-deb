#!/bin/bash
rm run
source guython-venv/bin/activate
python3 pyinst.py
deactivate
mv dist/run .
./run