from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main(): 
	if request.method=="GET": return render_template("login.html")
	elif request.method == "POST": 
		conn = sqlite3.connect("userinfo.db")
		c = conn.cursor()
		s = "SELECT email, password from users"
		login = False
		c.execute(s)
		for x in c.fetchall():
			if request.form['email'] == x[0] and request.form['password'] == x[1]:
				login = True
		if login == True:
			return render_template("logincomplete.html")
		elif login == False: 
			return render_template("loginfailed.html")
		
def create_user_id():
	conn = sqlite3.connect("userinfo.db")
	c = conn.cursor()
	s = "SELECT user_id from users where user_id like t_id"
	while True:
		opts = [i for i in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890']
		# 8 character long random hash
		t_id = [random.choice(opts) for i in range(8)]
		c.execute(s)
		if len(c.fetchall()) == 0:
			return t_id

# Criteria for valid account:
# Firstname: Only letters or hyphens, capital or lowercase
# Lastname: Only letters or hyphens, capital or lowercase
# securityquestion: Honestly we should just have a bunch of presets. I'm (Carter) not a huge fan of security questions, I would just prefer to have an email password reset.
# securityquestionanswer: Alphanumeric + special characters not including '" and \
# password: Alphanumeric + special characters not including '" and \
# email: valid email format... *******@*****.***
@app.route('/createanaccount',methods=["GET","POST"])
def createanaccount():
	if request.method=="GET":
		return render_template('createaccount.html',error='')
	elif request.method=="POST":
		conn = sqlite3.connect("userinfo.db")
		c = conn.cursor()
		nid = create_user_id()
		email = request.form['email']
		parts = email.split('@')
		if len(parts) != 2:
			return render_template('createaccount.html',error='email')
		if len(parts[1].split('.')) < 2:
			return render_template('createaccount.html',error='email')
		password = request.form['password']
		if '\'' in password or '\\' in password or '"' in password:
			return render_template('createaccount.html',error='password')
		namechars = [i for i in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-']
		fname = request.form['FN']
		lname = request.form['LN']
		cond = False
		for i in fname:
			if i not in namechars:
				cond = True
		for i in lname:
			if i not in namechars:
				cond = True
		if cond:
			return render_template('createaccount.html',error='names')
		sql = "INSERT into users (user_id, email, password, securityquestion, securityquestionanswer, Firstname, Lastname) values ("+ str(nid) + ", '" + str(email) + "', '" + str(password) + "', '" + str(request.form['SQ']) + "', '" + str(request.form['SA']) + "', '" + str(fname) + "', '" + str(lname) + "')"		
		c.execute(sql)
		conn.commit()
		conn.close()
		return render_template('accountcreated.html')
		
@app.route('/transaction',methods=['POST'])
def transaction():
	sender = request.form['sender']
	reciever = request.form['reciever']
	status = request.form['status']
	timestamp = request.form['timestamp']
	amount = request.form['amount']
	conn = sqlite3.connect("userinfo.db")
	c = conn.cursor()
	s = "SELECT balance from users where user_id like sender"
	c.execute(s)
	a = c.fetchall()
	if len(a) != 1:
		#TODO: Update transaction status
		return "ERROR: not exactly one user with id " + sender
	a = a[0]
	if a < amount:
		#TODO: Update transaction status
		return "TRANSACTION FAILED: insufficient funds"
	return sender