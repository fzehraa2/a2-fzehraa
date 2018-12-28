
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file, request
from hashlib import sha256

@route('/static')
def static_file_callback(filename):
    return static_file(filename, root="static")


def htmlify_CHESS(text):
    page = """
        <!DOCTYPE html>
<html>
	<head lang="en">
		<title>CHESS</title>
		<meta charset="utf-8">
		<link href="style.css" rel="stylesheet" type="text/css">
	</head>


<body bgcolor="lightblue" body color="white">
	<table width="902" height="1000" border="1" align=center bgcolor="white">
	<tr> 
	<td colspan="4" height="250"> <img src="chess.png"> </td>
	</tr>
	<tr>
	<td height="100" style= "font-size:32pt"> <a href="CHESS.html" >HOME</a></td> <td style= "font-size:32pt"><a href="x.html">BENEFITS</a> </td><td style= "font-size:32pt"><a href="m.html">HISTORY</a> </td> 
	</tr>
	<td height="500" colspan=3> 
		<ul style="font-size:32pt">
			<li>I have been playing chess since the day i met it thanks to my brother. It is one of my favorite game.</li>
			<li>It is a really enjoyable and beneficial for brain. You can have fun with your family or friends and can improve your thinking skills by playing chess.</li>
			<li>I could say that my thinking way has got a lot of changes because of playing chess and it taught me many tricks which can also be used in the real life.</li>
			
		
		</ul>
	
	</td>
	<tr>
	
	</table>
	<br> <br> <br> <br>
		
		<div class="alt" style= "font-size:32pt">
				<ul>
					<li>Fatma Zehra Postallı</li>
					<li>150170007</li>
					<li><a href="https://ituis18.github.io/a1-fzehraa">GitHub</a></li>
					<li>Mail
						<ul>
							<li><i>postalli17@itu.edu.tr</i></li>
							<li><i>zehrapostalli@gmail.com</i></li>
						</ul>
					</li>
				</ul>
			</div>

</body>


</html>

    """ % (text)
    return page

def index():
    return htmlify("My lovely website",
                   "Hey man!This is going to be an awesome website, when it is finished.")

route('/', 'GET', index)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

