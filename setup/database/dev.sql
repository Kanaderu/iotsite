-- create user `geo` with password `geo`
CREATE USER geo WITH ENCRYPTED PASSWORD 'geo';

-- create database
CREATE DATABASE geodjango with OWNER geo;

-- setup user with permissions to database
GRANT ALL PRIVILEGES ON DATABASE geodjango TO geo;

-- select database
\c geodjango;

-- enable postgis extension
CREATE EXTENSION postgis;

-- drop database
--DROP DATABASE geodjango;
