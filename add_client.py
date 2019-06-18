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
uname=web_data.getvalue('uname')
conn=mariadb.connect(user='root',password='q',database='autolab',host='localhost')
cursor=conn.cursor()
cursor.execute('select uip from user where uip="{}";'.format(uip))
out=cursor.fetchall()
if len(out)>0:
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>CLIENT ALREADY EXISTS</h1></center></body>"
	print  "<meta http-equiv='refresh' content='3;http://127.0.0.1/AutoLab/add_client.html'>"

else :
	cursor.execute('insert into user (uip,password,uname)values("{}","{}","{}");'.format(uip,password,uname))
	conn.commit() 
	commands.getoutput('ssh-keygen')
	commands.getoutput('ssh-copy-id "{}"')
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>CLIENT ADDED SUCCESSFULLY</h1></center></body>"
	print "<meta http-equiv='refresh' content='3;http://127.0.0.1/AutoLab/explore.html'>"






