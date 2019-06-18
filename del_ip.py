#!/usr/bin/python2

import cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb
print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

conn=mariadb.connect(host='localhost',user='root',password='q',database='autolab')
cursor=conn.cursor()
value=web_data.getlist("machine")
if value==[]:
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>No client selected</h1></center></body>" 
	print  "<meta http-equiv='refresh' content='1;http://127.0.0.1/cgi-bin/AutoLAB/delete.py'>"
else:

	f=open('/var/www/cgi-bin/AutoLAB/inventory.txt','w')
	f.write("[group1]\n")

	for i in value:
		cursor.execute('select * from user where uname="{}";'.format(i))
		out=cursor.fetchall()
	
		if len(out)>0:
			for row in out:
				f.write(row[1])
				f.close();
		print  "<meta http-equiv='refresh' content='1;http://127.0.0.1/AutoLab/del_app.html'>"
	
		
