#!/bin/bash

# Ubuntu setup, refer to https://docs.djangoproject.com/en/2.2/ref/contrib/gis/install/geolibs/ for other distributions
sudo apt-get install binutils libproj-dev gdal-bin

# GeoIP2
# https://docs.djangoproject.com/en/2.2/ref/contrib/gis/geoip2/
# https://github.com/maxmind/libmaxminddb
sudo add-apt-repository ppa:maxmind/ppa
sudo apt update
sudo apt install libmaxminddb0 libmaxminddb-dev mmdb-bin

sudo apt install postgis
