#!/bin/bash

virtualenv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt


#python setup.py sdist
#twine upload dist/*
