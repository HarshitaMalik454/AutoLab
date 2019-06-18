#!/usr/bin/python2

import cgi,cgitb,commands
cgitb.enable()
import mysql.connector as mariadb
print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

conn=mariadb.connect(host='localhost',user='root',password='q',database='autolab')
cursor=conn.cursor()
value=web_data.getlist("machine")
if value==[]:
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1>"
	print "No client selected"
	print "</h1></center></body>"
	 
else: 

	for i in value:
		cursor.execute('select uip from user where uname="{}";'.format(i))
		out=cursor.fetchall()
	
		cursor.execute('delete from user where uname="{}"'.format(i))
		conn.commit()
			 
		print "<body style="'background-color:linen;padding-top:100px;'"><center><h1>"
		print " User Removed."
		print "</h1></center></body>"
print "<meta http-equiv='refresh' content='3;http://127.0.0.1/AutoLab/explore.html'>"	

		
	
