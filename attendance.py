from datetime import datetime
from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
ENV = 'prod'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ROOT@localhost/Attendance'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dmuctaiwtifxzb:1b7f129f82d1e95ac1d6e691da2d885684fcca0f790fbab65ccc6d4ed89e2b47@ec2-34-201-95-176.compute-1.amazonaws.com:5432/d1edcsllbhh58s'

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