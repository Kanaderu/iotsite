#!/bin/bash

# refer to https://postgis.net/install/ for additional information

# Ubuntu
#https://wiki.ubuntu.com/UbuntuGIS
#https://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS24UbuntuPGSQL10Apt

sudo apt-get install python-software-properties
sudo add-apt-repository ppa:ubuntugis/ppa

sudo apt install postgres
sudo apt install postgis

# setup database
sudo psql -h localhost -U postgres -a -f postgis.sql
