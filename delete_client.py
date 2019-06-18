#!/usr/bin/python2

import cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb
import commands
print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

uip= web_data.getvalue('uip')
password= web_data.getvalue('password')
conn=mariadb.connect(user='root',password='q',database='autolab',host='localhost')
cursor=conn.cursor()
cursor.execute('select uip from user where uip="{}";'.format(uip))
out=cursor.fetchall()
if len(out)>0:
	cursor.execute('delete from user where uip="{}");'.format(uip,password))
	conn.commit() 
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>"
	print " User Removed."
	print "</h1></center></body>"
	print "<meta http-equiv='refresh' content='3;http://127.0.0.1/AutoLab/explore.html'>"	

else :
	
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>"
	print " User Doesn't Exists."
	print "</h1></center></body>"
	print  "<meta http-equiv='refresh' content='3;http://127.0.0.1/delete_client.html'>"
	

