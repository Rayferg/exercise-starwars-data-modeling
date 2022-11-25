import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()




class User(Base):
    __tablename__ = 'user'
    id= Column(Integer, primary_key=True)
    username = Column(String(18))
    firstname = Column(String(14), nullable=False)
    lastname = Column(String(18), nullable=False)
    email = Column(String(30))
    password = Column(String(14), nullable=False)
 
    def to_dict(self):
     return {}

class Character(Base):
    __tablename__='character'
    id= Column(Integer, primary_key=True)
    name= Column(String(18))
    age = Column(Integer)
    race = Column(String(30))
    eyecolor = Column(String(10))
    birthplaceid = Column(Integer, ForeignKey('Planet.id')) #reference frame key
    birthplace = relationship('Planet', foreign_keys = [birthplaceid])

    def to_dict(self):
     return {}

class Planet(Base):
    __tablename__= "planet"
    id = Column(Integer, primary_key=True)
    size = Column(String(10))
    atmosphere = Column(String(10))
    name = Column(String(10))
    climate = Column(String(10))

    def to_dict(self):
     return {}
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey(User.id))
    characterid = Column(Integer, ForeignKey(Character.id))
    planetid = Column(Integer, ForeignKey(Planet.id))
    user= relationship('User', foreign_keys =[userid])
    character = relationship('Character')
    planet = relationship('Planet')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
