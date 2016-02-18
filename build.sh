#!/bin/bash

rm bundle.zip

zip -9 bundle.zip lambda_handler.py

cd .env/lib/python2.7/site-packages && zip -r9 ../../../../bundle.zip *
