#!/bin/bash

DEVICE_ADDRESS=192.168.1.111

while true; do
	rsync -rvp . root@$DEVICE_ADDRESS:/usr/share/enigma2/display/alpha
	ssh root@$DEVICE_ADDRESS -f '/usr/local/bin/enigma2_run /home/root/scripts/lcd_test.py'
	sleep .8
	scp root@$DEVICE_ADDRESS:/tmp/lcd.png /dev/shm/lcd2.png;mv /dev/shm/lcd2.png /dev/shm/lcd.png
	inotifywait . -e close_write,moved_to
	sleep .1
done
