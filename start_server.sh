#!/bin/bash
uwsgi --ini iotsite/uwsgi.ini --enable-threads --thunder-lock
