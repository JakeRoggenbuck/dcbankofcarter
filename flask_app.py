from flask import Flask, render_template, request
import sqlite3
from random import randint

app = Flask(__name__)

@app.route('/')
def main(): return render_template('login.html')

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
		sql = "INSERT into users (user_id, email, password, securityquestion, securityquestionanswer)values ("+ str(id) + ", '" + str(request.form['email']) + "', '" + str(request.form['password']) + "', '" + str(request.form['SQ']) + "', '" + str(request.form['SA']) + "')"		
		c.execute(sql)
		conn.commit()
		conn.close()
		return render_template('accountcreated.html')
		
@app.route('/transaction',methods=['POST'])
def transaction():
	sender = request.form['sender']
	return sender