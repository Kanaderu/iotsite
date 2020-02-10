#!/bin/bash

make html
mv -f build/html/* ../
rm -rf build
git add ../*

git commit -m "Update `date`"
git push
