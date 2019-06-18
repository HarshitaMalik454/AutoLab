#!/usr/bin/python2

import cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb

print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

conn=mariadb.connect(host='localhost',user='root',password='q',database='autolab')
cursor=conn.cursor()

cursor.execute('select * from user;')
out=cursor.fetchall()
if len(out)>0:
	html='''
<!DOCTYPE html><html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Select PC | AutoLAB</title>
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
 
                        <li><a href = "http://127.0.0.1/cgi-bin/AutoLAB/profile.py"><span class = "glyphicon glyphicon-user"></span> Your Profile</a></li>
                        <li><a href = "http://127.0.0.1/AutoLab/index.html"><span class = "glyphicon glyphicon-log-in"></span> Logout</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="container" id="content">

            <!-- Jumbotron Header -->
            <div class="jumbotron home-spacer" id="products-jumbotron">
              <center>
		  <h2>ADD CLIENT FOR APP DELETION!</h2>
                  	      </center>
            </div>
         
			
      <form action="del_ip.py" method="POST">
		 <div class="row text-center" id="item_list">
                    
'''
	print html
	for row in out:
		
		rep='''<div class="col-sm-4">
                            <div class="thumbnail">
                                <img src="http://127.0.0.1/AutoLab/img/machine.png" alt="no image">
                                <div class="caption">'''
		print rep
                print'<input type="checkbox" name="machine" value="{}"><b>"{}"</b></input>'.format(row[3],row[3])
				 
						
                div=       '''  </div>
                            </div> 
                    </div>'''
		

		print div
	htm='''
 </div>
            </div>
            <!--Item categories listing end-->

<center><button type="submit" name="submit" class="btn btn-primary btn-lg">Submit</button><br><br></center>
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
else:
	print "<body style="'background-color:linen;padding-top:100px;'"><center><h1>"
	print "NO CLIENT AVAILABLE"  
	print "<meta http-equiv='refresh' content='2;http://127.0.0.1/AutoLab/explore.html'>"
	print "</h1></center></body>"
