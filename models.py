# -*- coding: utf-8 -*-
from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from passlib.apps import custom_app_context as pwd_context


Base = declarative_base()


class Restaurant(Base):
  __tablename__ = 'restaurant'
  id = Column(Integer, primary_key = True)
  restaurant_name = Column(String)
  restaurant_address = Column(String)
  restaurant_image = Column(String)
  
  
  #Add a property decorator to serialize information from this database
  @property
  def serialize(self):
    return {
      'restaurant_name': self.restaurant_name,
      'restaurant_address': self.restaurant_address,
      'restaurant_image' : self.restaurant_image,
      'id' : self.id
      
      }

class User(Base):
  __tablename__ = 'user'
  #defining columns for tblUser
  id = Column(Integer, primary_key = True)
  user_alias = Column(String(64))
  password_hash = Column(String(64))
  email = Column(String)

  #Method to hash User Password
  def hash_password(self, password):
    self.password_hash = pwd_context.encrypt(password)

  def verify_password(self, password):
    return pwd_context.verify(password, self.password_hash)

  #Add a property decorator to serialize information from this database
  @property
  def serialize(self):
    return {
      'user_alias': self.user_alias,
      'password_hash': self.password_hash,
      'email': self.email,
      'id' : self.id  
    }
  
class Request(Base):
    __tablename__ = 'request'
    id = Column(Integer, primary_key = True)
    mealType = Column(String)
    location = Column(String)
    restaurant_name = Column(String)
    restaurant_address = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    mealTime = Column(String)
    filled = Column(String)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'mealType': self.mealType,
            'mealTime': self.mealTime,
            'location': self.location,
            'restaurant_name': self.restaurant_name,
            'restaurant_address': self.restaurant_address,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'filled': self.filled,
            'user_id': self.user_id
        }

class Proposal(Base):
  __tablename__ = 'tblProposal'
  #defining columns for tblProposal
  id = Column(Integer, primary_key = True)
  filled = Column(String)
  user_proposed_to = Column(Integer)
  user_proposed_from = Column(Integer)
  request_id = Column(Integer, ForeignKey('request.id'))
  request = relationship(Request)
  #Add a property decorator to serialize information from this database
  @property
  def serialize(self):
    return {
      'id': self.id,
      'user_proposed_to': self.user_proposed_to,
      'user_proposed_from' : self.user_proposed_from,
      'filled' : self.filled,
      'request_id' : self.request_id
      }

class MealDate(Base):
  __tablename__ = 'tblMealDate'
  #defining columns for tblMealDate
  id = Column(Integer, primary_key = True)
  user_1 = Column(String)
  user_2 = Column(String)
  restaurant_name = Column(String)
  restaurant_address = Column(String)
  meal_time = Column(String)
  #Add a property decorator to serialize information from this database
  @property
  def serialize(self):
    return {
      'id': self.id,
      'user_1': self.user_1,
      'user_2' : self.user_2,
      'restaurant_name' : self.restaurant_name,
      'restaurant_address' : self.restaurant_address,
      'meal_time' : self.meal_time
      }


engine = create_engine('sqlite:///meetup.db')
Base.metadata.create_all(engine)      