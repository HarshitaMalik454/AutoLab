#!/usr/bin/python2

import cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb

print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()
ia=web_data.getvalue('Install App')
da=web_data.getvalue('Delete App')
ac=web_data.getvalue('Add Client')
rc=web_data.getvalue('Remove Client')
ss=web_data.getvalue('Shutdown System')

if ia == 1 :
	print "<meta http-equiv='refresh' content='0;http://127.0.0.1/AutoLAB/ip_install.html'>" 
if da == 1 :
	print "<meta http-equiv='refresh' content='0;http://127.0.0.1/AutoLAB/ip_delete.html'>" 
if ac == 1 :
	print "<meta http-equiv='refresh' content='0;http://127.0.0.1/AutoLAB/ip_add.html'>" 
if rc == 1 :
	print "<meta http-equiv='refresh' content='0;http://127.0.0.1/AutoLAB/ip_remove.html'>" 
if ss == 1 :
	print "<meta http-equiv='refresh' content='0;http://127.0.0.1/AutoLAB/ip_shut.html'>" 



