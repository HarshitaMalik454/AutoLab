#!/usr/bin/python2

import cgi,cgitb,commands,os
cgitb.enable()
import mysql.connector as mariadb
print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

conn=mariadb.connect(host='localhost',user='root',password='q',database='autolab')
cursor=conn.cursor()
value=web_data.getlist("machine")
if value == [] :
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1>"
	print "No client selected" 
	print "</h1></center></body>"
	print "<meta http-equiv='refresh' content='3;http://127.0.0.1/cgi-bin/AutoLAB/shut.py'>"
else :
	for i in value:
		cursor.execute('select uip,uname from user where uname="{}";'.format(i))
		out=cursor.fetchall()
	
		if len(out)>0:
			f=open('/var/www/cgi-bin/AutoLAB/inventory.txt','w')
			f.write("[group1] \n")
			for row in out:
					f.write(row[0])
					f.close();
			i=commands.getoutput('sudo ansible group1 -i /var/www/cgi-bin/AutoLAB/inventory.txt -a "systemctl poweroff"')
			
			if i.count("changed")==1 :
				print "<body style="'background-color:linen;padding-top:100px;'"><center><h1>"
				print row[1]
				print " successfully shutdown."
				print "</h1></center></body"
				
	
				
			else :
				print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>HOST UNREACHABLE</h1></center></body>"
				
		
				

	print  "<meta http-equiv='refresh' content='1;http://127.0.0.1/AutoLab/explore.html'>"

