-- create user `geo` with password `geo`
CREATE USER geo WITH ENCRYPTED PASSWORD 'geo';

-- Make geo a superuser
ALTER USER geo SUPERUSER;

-- Give geo ability to create databases
ALTER USER geo CREATEDB;

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
