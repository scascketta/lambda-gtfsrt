#!/usr/bin/env bash

set -ex

rm -rf bundle bundle.zip

mkdir -p bundle

pip install -r requirements.txt
cp -r .env/lib/python2.7/site-packages/* bundle
cp lambda_handler.py bundle

touch bundle/google/__init__.py

cd bundle

zip -r9 ../bundle.zip *

cd ..
