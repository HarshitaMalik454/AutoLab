#!/usr/bin/python2

import cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb
from flask import Flask, request, render_template

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

name= web_data.getvalue('name')
password= web_data.getvalue('password')

conn=mariadb.connect(host='localhost',user='root',password='q',database='autolab')
cursor=conn.cursor()

cursor.execute('select name from admin where name="{}";'.format(name))
nm=cursor.fetchall()
if len(nm)>0:
	cursor.execute('select password from admin where password="{}";'.format(password))
	ps=cursor.fetchall()
	if len(ps)>0:
		print  "<meta http-equiv='refresh' content='3;http://127.0.0.1/AutoLab/explore.html'>"
	else  :
		print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>"
		print "Password Incorrect"
		print "</h1>"
		print "<a href='http://127.0.0.1/AutoLab/login.html'>"
		print "Click here for redirection"
		print "</a></center></body>"

else :
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>"
        print "Incorrect Data"
        print "</h1>"
        print "<a href='http://127.0.0.1/AutoLab/login.html'>"
        print "Click here for redirection"
        print "</a></center></body>"

