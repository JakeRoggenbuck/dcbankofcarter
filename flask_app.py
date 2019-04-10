from flask import Flask, render_template, request
import sqlite3
from random import randint

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main(): 
	if request.method=="GET": return render_template("login.html")
	else: 	
		conn = sqlite3.connect("userinfo.db")
		c = conn.cursor()
		s = "SELECT email, password from users"
		login = False
		c.execute(s)
		for x in c.fetchall():
			if request.method['email'] == x[0] and request.method['password'] == x[1]:
				login = True
		if login == True:
			return render_template("logincomplete.html")
		else: 
			return render_template("loginfailed.html")		

@app.route('/createanaccount',methods=["GET","POST"])
def createanaccount():
	if request.method=="GET":
		return render_template('createaccount.html')
	elif request.method=="POST":
		conn = sqlite3.connect("userinfo.db")
		c = conn.cursor()
		sql = "SELECT user_id from users" 
		c.execute(sql)
		for x in c.fetchall():
			id = randint(1,10000)
			if id != x: break
		sql = "INSERT into users (user_id, email, password, securityquestion, securityquestionanswer, Firstname, Lastname)values ("+ str(id) + ", '" + str(request.form['email']) + "', '" + str(request.form['password']) + "', '" + str(request.form['SQ']) + "', '" + str(request.form['SA']) + "', '" + str(request.form['FN']) + "', '" + str(request.form['LN']) + "')"		
		c.execute(sql)
		conn.commit()
		conn.close()
		return render_template('accountcreated.html')
		
@app.route('/transaction',methods=['POST'])
def transaction():
	sender = request.form['sender']
	return sender