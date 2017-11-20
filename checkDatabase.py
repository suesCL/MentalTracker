from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataBaseSetup import Base, dailyInfo, symptons


engine = create_engine('sqlite:///mentalReport.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
  
  
dailyInfo.__table__.drop(engine)
# days = session.query(dailyInfo).all()
# print days
# for i in days:
	# print str(i.Date) + " " + str(i.StressLevel)
	# print "The end"

