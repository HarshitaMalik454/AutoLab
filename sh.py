#!/usr/bin/python2
import os
os.system('sudo ansible group1 -i /var/www/cgi-bin/AutoLAB/inventory.txt -a "poweroff"')

