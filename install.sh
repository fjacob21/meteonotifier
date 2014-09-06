#!/bin/sh

cp servo.py /etc/init.d/
cp meteonotifier /etc/init.d/
chmod 755 /etc/init.d/meteonotifier
update-rc.d meteonotifier defaults
