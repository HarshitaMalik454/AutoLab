#!/usr/bin/python2

import cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb

print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

conn=mariadb.connect(host='localhost',user='root',password='q',database='autolab')
cursor=conn.cursor()

cursor.execute('select * from admin order by sid desc limit 1;')
out=cursor.fetchall()
if len(out)>0:
	
	html='''
<!DOCTYPE html><html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Your Profile | AutoLAB</title>
        <link href="http://127.0.0.1/AutoLab/css/bootstrap.min.css" rel="stylesheet">
        <link href="http://127.0.0.1/AutoLab/css/style.css" rel="stylesheet">
        <script src="http://127.0.0.1/AutoLab/js/jquery.js"></script>
        <script src="http://127.0.0.1/AutoLab/js/bootstrap.min.js"></script>
    </head>

     <body>
        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>                        
                    </button>
                    <a class="navbar-brand" href="http://127.0.0.1/AutoLab/index.html"><span class="glyphicon glyphicon-home"></span> AutoLAB</a>
                </div>
                <div class="collapse navbar-collapse" id="myNavbar">
                    <ul class="nav navbar-nav navbar-right">
 
                        <li><a href = "http://127.0.0.1/AutoLab/index.html"><span class = "glyphicon glyphicon-log-in"></span> Logout</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="container" id="content">

            <!-- Jumbotron Header -->
            <div class="jumbotron home-spacer" id="products-jumbotron">
              <center>
		  <h2>Hello Server!</h2>
                  	      </center>
            </div>
         
		<div class="panel-body">
                                <p class="text-warning"><i>Your Profile is Here!</i><p>
                                    <div class="form-group">
                                        '''
	print html       
	
	for row in out:
		sid=row[0]
		print "<h3>Name:"
		print row[1]
		print "</h3>"
		print "<h3>IP Address:"
		print row[2]
		print "</h3>"
		print "<h3>Password:"
		print row[3]
		print "</h3>"
		print "<h3>Contact No:"
		print row[4]
		print "</h3>"
		print "<h3>Email Address:"
		print row[5]
		print "</h3>"
		
        h='''</div>
                                    

                                </form><br/>
                            </div>
                            <div class="panel-footer"><p>Delete Account <a href="del_account.py">Click Here</a></p></div>
                        </div>
                    </div>
                    
'''
	print h
	

	
		
		




	htm='''
 </div>
            </div>
            

</table>
	 
	</form>
	<footer>
            <div class="container">
                <center>
                    <p>Copyright &copy; AutoLAB. All Rights Reserved  |  Contact Us: +91 9772139728  +918755366285</p>	
                </center>
            </div>
        </footer>
    </body>
</html>'''
	print htm
