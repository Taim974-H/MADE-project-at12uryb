#!/bin/bash

# install requirements
python -m pip install -r ./project/src/requirements.txt
# Run the pytest script
python ./project/src/tests.py