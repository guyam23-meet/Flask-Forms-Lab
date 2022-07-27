from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
#sapp.config['SECRET_KEY'] = 'super-secret-key'


username = "(╯°□°）╯︵ ┻━┻"
password = "flip"
facebook_friends=["Never","Gonna","Give", "You", "Up"]


@app.route('/',methods=["GET","POST"])  # '/' for the default page
def login():
	if request.method=="POST":
		if request.form['username']==username and request.form['password']==password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html',fb=facebook_friends)

@app.route('/friend_exists/<string:name>',methods=["GET","POST"])
def friend_exist(name):
	return render_template('friend_exists.html',name=name,fb=facebook_friends)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)