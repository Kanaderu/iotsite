#!/bin/bash

make html
mv build/html/* ../
rm -rf build
git add ../*

git commit -m "Update `date`"
git push
