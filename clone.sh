#!/bin/bash

git clone https://github.com/S3gam/EDEM-Data-Analytics.git ./desktop

touch ./EDEM-Data-Analytics/hola.txt

git init

git add .

git commit -m "first commit"

git remote add origin https://github.com/S3gam/EDEM-Data-Analytics.git

git push -u origin master

