from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataBaseSetup import Base, dailyInfo, symptons
import datetime

app = Flask(__name__)
engine = create_engine('sqlite:///mentalReport.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/', methods=['GET', 'POST'])
def rateLevels():
	if request.method == 'POST':
		if request.form['HighStress']:
			newRecord = dailyInfo(Date = datetime.date.today(), StressLevel = request.form['HighStress'])
			session.add(newRecord)
			session.commit()
		elif request.form['LowStress']:
			newRecord = dailyInfo(Date = datetime.date.today(), StressLevel = request.form['LowStress'])
			session.add(newRecord)
			session.commit()
		else:
			newRecord = dailyInfo(Date = datetime.date.today(), StressLevel = request.form['MediumStress'])
			session.add(newRecord)
			session.commit()
			
		return redirect(url_for('rateLevels'))
	else: 
		return render_template('rateLevels.html')
	

	

if __name__ == '__main__':
    app.secret_key = 'super_secure_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)