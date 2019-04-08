from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/transaction',methods=['POST'])
def transaction():
	sender = request.form['sender']
	return sender