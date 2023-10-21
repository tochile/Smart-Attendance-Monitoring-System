
from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml
import numpy as np
#import face_recognition 
#import os
#import cv2


app = Flask(__name__) 
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login',methods=['POST'])
def login():
    
    username = request.form['username']
    password = request.form['password']
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * from Users where binary username=%s and binary password=%s",[username,password])
    if(result>0):
        return render_template("login.html", username=username)
    else:
        error = 'failed'
        return render_template("index.html", error=error)


           

        
if __name__ == '__main__':
	app.run(debug=True)
