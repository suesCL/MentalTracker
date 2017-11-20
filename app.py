from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataBaseSetup import Base, Daily_Level, Daily_Symptom, Symptom, Category
import datetime

app = Flask(__name__)
engine = create_engine('sqlite:///mentalReport.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/', methods=['GET', 'POST'])
def rateLevels():
	if request.method == 'POST':
		if request.form['MediumStress']:
			newRecord = Daily_Level(Date = datetime.date.today(), StressLevel = request.form['MediumStress'])
			
		if request.form['LowStress']:
			newRecord = Daily_Level(Date = datetime.date.today(), StressLevel = request.form['LowStress'])
			
		if request.form['HighStress']:
			newRecord = Daily_Level(Date = datetime.date.today(), StressLevel = request.form['HighStress'])
		session.add(newRecord)
		session.commit()
		return redirect(url_for('rateLevels'))
	else: 
		return render_template('rateLevels.html')
	

	

if __name__ == '__main__':
    app.secret_key = 'super_secure_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)