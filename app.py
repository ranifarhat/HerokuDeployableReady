from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
# from databases import *
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"



@app.route("/")
def home():
	return render_template("home.html")


@app.route("/he")
def home_hebrew():
	return render_template("home_hebrew.html")

@app.route("/ar")
def home_arabic():
	return render_template("home_arabic.html")



if __name__ == '__main__':
	app.run(debug=True)