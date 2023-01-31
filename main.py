from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def greeting():
   if request.method == 'GET':
       return render_template("index.html")

@app.route('/kontakty', methods=['GET'])
def kontakty():
   if request.method == 'GET':
       return render_template("kontakty.html")
