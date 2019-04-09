from flask import Flask, render_template, request
import sqlite3

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
		sql = "INSERT into users (user_id, email, password, securityquestion, securityquestionanswer)"
		sql += "values (79817, " + str(request.form['email']) + ", " + str(request.form['password']) + ", " + str(request.form['SQ']) + ", " + str(request.form['SA']) + ")"
		c.execute(sql)
		conn.close()
		return render_template('accountcreated.html')
		
@app.route('/transaction',methods=['POST'])
def transaction():
	sender = request.form['sender']
	return sender