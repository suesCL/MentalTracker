import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()

#create table called Daily_Level which contains general mental info for the day
class Daily_Level(Base):
    __tablename__ = 'Daily_Level'

    id = Column(Integer, primary_key=True)
    #Date = Column(Text, unique = True)
    Date = Column(Text)
    
    # level 0 to 4 (from low to high) 
    #StressLevel = Column(Integer, nullable = False)
    StressLevel = Column(Integer)
    AnxietyLevel = Column(Integer)
    DepressionLevel = Column(Integer)
    
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'Date': self.Date,
            'StressLevel' : self.StressLevel,
            'AnxietyLevel' : self.AnxietyLevel,
            'DepressionLevel' : self.DepressionLevel
        }


class Daily_Symptom(Base):
    __tablename__ = 'Daily_Symptom'

    id = Column(Integer, primary_key=True)
    
    SymptomID = Column(Integer, ForeignKey('Symptom.id')
    Symptom = relationship(Symptom)
    
    DateID = Column(Integer, ForeignKey('Daily_Level.id'))
    date = relationship(Daily_Level)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'SymptomID': self.SymptomID,
            'DateID' : self.DateID,           
        }
        
        
class Symptom(Base):
    __tablename__ = 'Symptom'

    id = Column(Integer, primary_key=True)
    symptom = Column(String(250), nullable = false)
    
    categoryID = Column(Integer)
    category = relationship(Category)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'sympton': self.sympton,
            'categoryID' : self.categoryID
        }
        
        
    
class Category(Base):
    __tablename__ = 'Category'

    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable = false)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'category' : self.category
        }

        
class User(Base):
    __tablename__ = 'user_info'
    
    id = Column(Integer, primary_key = True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))
    email = Column(String(250), nullable = False)
    
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


        
        
engine = create_engine('sqlite:///mentalReport.db')


Base.metadata.create_all(engine)
