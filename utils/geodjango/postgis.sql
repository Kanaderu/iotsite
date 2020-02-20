-- Create user "geo" with password "geo"
CREATE USER geo WITH ENCRYPTED PASSWORD 'geo';

-- Create database geodjango
CREATE DATABASE geodjango with OWNER geo;
\c geodjango
GRANT ALL PRIVILEGES ON DATABASE geodjango TO geo;

-- Enable postgis extension
CREATE EXTENSION postgis;
