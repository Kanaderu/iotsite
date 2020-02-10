#!/bin/bash

make html
rm -r ../_sources ../_static
mv -f build/html/* ../
rm -rf build
git add ../*

git commit -m "Updated `date`"
git push
