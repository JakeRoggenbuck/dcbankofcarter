from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def main(): return render_template('login.html')

@app.route('/createanaccount',methods=["GET","POST"])
def createanaccount():
	if request.method=="GET":
		return render_template('createaccount.html')
	if request.method=="POST":
		return render_template('accountcreated.html')
@app.route('/transaction',methods=['POST'])
def transaction():
	sender = request.form['sender']
	return sender