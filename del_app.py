#!/usr/bin/python2
import cgi,cgitb,os,commands
cgitb.enable()
print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

value=web_data.getlist("app")
if value == [] :
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>NO APPLICATION SELECTED</h1></center></body>"
	print "<meta http-equiv='refresh' content='2;http://127.0.0.1/AutoLab/del_app.html'>"
else :
	f=open('/var/www/cgi-bin/AutoLAB/playbook.yml','w+')
	f.write("---\n - hosts: group1 \n   tasks:")
	for i in value:
		f=open('/var/www/cgi-bin/AutoLAB/playbook.yml','a')
		f.write("\n    - name: remove ")
		f.write(i)
		f.write("\n      yum:\n        name: ")
		f.write(i)
		f.write("\n        state: absent")
		f.close();
	i=commands.getoutput("sudo ansible-playbook playbook.yml -i /var/www/cgi-bin/AutoLAB/inventory.txt")
	
	if i.count("changed=1")==1 :
		print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>ONE APPLICATION DELETED</h1></center></body>"
	elif i.count("changed=2")==1 :
		print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>TWO APPLICATIONS DELETED</h1></center></body>"
 	elif i.count("changed=3")==1 :	
		print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>THREE APPLICATIONS DELETED</h1></center></body>"
	elif i.count("unreachable=1")>=1 :
		print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>HOST UNREACHABLE</h1></center></body>"
	else :
		print "<body style="'background-color:linen;padding-top:100px;'"><center><h1 style="'color:blue;'"><h1>APPLICATION DOES NOT EXIST</h1></center></body>"
		
	print "<meta http-equiv='refresh' content='2;http://127.0.0.1/AutoLab/explore.html'>"



		

	
