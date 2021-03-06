import re
from django.shortcuts import render
from flask import Flask, redirect,  url_for, render_template, request,flash, session
import sqlite3 as sql
from log import *
from user import *
from tracker import *


app = Flask(__name__)
app.secret_key="ravali"


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/insertnewuser',methods = ['POST'])
def insertuser():
   return adduser()

@app.route('/dashboard',methods = ['POST'])
def chckuser():
   return checkuser()

@app.route('/newtracker')
def newtracker():
   return render_template('createtracker.html')

@app.route('/insertnewtracker',methods = ['POST'])
def inserttracker():
   return addtracker()

@app.route('/log/<int:trackerid>/<string:trackername>')
def insertlog(trackerid: int, trackername: str):
   return render_template('addlog.html',ti=trackerid, tn=trackername)

@app.route('/addlog', methods =['POST','GET'])
def newlog():
   return addlog()

@app.route('/tracker/<int:trackerid>')
def trackerdisp(trackerid:int):
   return logtable(tid= trackerid)

@app.route('/trackerdelete/<int:trackerid>')
def deletetracker(trackerid:int):
   return deltracker(tid=trackerid)

@app.route('/trkredit/<int:trackerid>')
def editrkr(trackerid:int):
   return trkedit(tid=trackerid)

@app.route('/trackeredit', methods = ['POST'])
def edittracker():
   return editracker()

@app.route('/logdelete/<int:logid>')
def deletelog(logid:int):
   return dellog(lid=logid)

@app.route('/lgedit/<int:logid>')
def editlg(logid:int):
   return logedit(lid=logid)

@app.route('/logedit', methods = ['POST'])
def editlog():
   return edtlog()

@app.route('/logout')
def logout():
   session['usrid']= ''
   return render_template('login.html')


if __name__=='__main__':
    app.run(debug= True)

