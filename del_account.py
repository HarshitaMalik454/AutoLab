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
cursor.execute('select * from admin order by sid desc limit 1;')
out=cursor.fetchall()
for row in out:
	cursor.execute('delete from admin where sip="{}";'.format(row[2]))
	conn.commit()
print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>ACCOUNT SUCCESSFULLY DELETED</h1></center></body>"
print  "<meta http-equiv='refresh' content='2;http://127.0.0.1/AutoLab/index.html'>"
