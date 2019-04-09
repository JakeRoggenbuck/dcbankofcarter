from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def main(): return render_template('login.html')
@app.route('/transaction',methods=['POST'])
def transaction():
	sender = request.form['sender']
	return sender