from datetime import datetime
from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from Frame import get_frame
import Frame
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/home')
def home():
    get_frame(False)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=False)
    
