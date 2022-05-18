from datetime import datetime
from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy

# https://github.com/J-A-M-E-5/heroku16-buildpack-python-opencv-dlib.git

app = Flask(__name__)
ENV = 'prod'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ROOT@localhost/Attendance'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tgccsusylervho:43f523cc6be683379749e80a571f5bbaa971b0b4433a7102c4f96e4cab469eb4@ec2-54-204-56-171.compute-1.amazonaws.com:5432/d2qvn354cn9ils'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
time_now = datetime.now()
tStr = time_now.strftime('%H:%M:%S')
dStr = time_now.strftime('%d_%m_%Y') 
attendance_sheet = "Attendance_" + dStr 

class Record(db.Model):
    __tablename__ = attendance_sheet
    Name = db.Column(db.String(200) , primary_key = True)
    Time = db.Column(db.String(200))
    def __init__(self,Name,Time):
        self.Name = Name
        self.Time = Time
        

def attendance(name):
    db.create_all()
    data = Record(name, tStr)
    try:
        db.session.add(data)
    except :
        pass
    db.session.commit()