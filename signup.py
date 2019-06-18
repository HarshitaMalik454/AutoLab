#!/usr/bin/python2

import cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb

print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

name= web_data.getvalue('sname')
sip= web_data.getvalue('sip')
password= web_data.getvalue('password')
contact= web_data.getvalue('contact')
email= web_data.getvalue('email')

conn=mariadb.connect(user='root',password='q',database='autolab',host='localhost')
cursor=conn.cursor()
cursor.execute('select sip from admin where sip="{}";'.format(sip))
out=cursor.fetchall()
if len(out)>0:
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>"
	print "IP Already Exists."
	print "</h1></center></body>"
	print  "<meta http-equiv='refresh' content='3;http://127.0.0.1/AutoLab/signup.html'>"

else :
	cursor.execute('insert into admin (name,sip,password,contact,email)values("{}","{}","{}","{}","{}");'.format(name,sip,password,contact,email))
	conn.commit() 
	print "<meta http-equiv='refresh' content='3;http://127.0.0.1/AutoLab/explore.html'>"


