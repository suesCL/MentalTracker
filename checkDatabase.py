from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataBaseSetup import Base, Daily_Level, Daily_Symptom, Symptom, Category


engine = create_engine('sqlite:///mentalReport.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
  

days = session.query(Daily_Level).all()
print days
for i in days:
	print str(i.Date) + " " + str(i.StressLevel)
	print "The end"

