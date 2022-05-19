from datetime import datetime
from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ROOT@localhost/Attendance'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kcigqbolhiwzac:4aa84993e1e93a2a190de02fab7ff0b2b2839d8c1b7701e2d502eb5ba8507623@ec2-3-211-6-217.compute-1.amazonaws.com:5432/db72hsh44qc9ck'

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
    data = Record(name, time_now.strftime('%H:%M:%S'))
    try:
        db.session.add(data)
    except :
        pass
    db.session.commit()