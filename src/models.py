import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String (250), nullable=False)
    last_name = Column(String (250))
    user_name = Column(String (250), nullable=False)
    password = Column(String (250), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_name

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String (250))
    url = Column(String (250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String (250))
    skin_color = Column(String (250), nullable=False)
    eye_color = Column(String (250), nullable=False)
    birth_year = Column(String (250), nullable=False)
    gender = Column(String (250))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String (250))
    url = Column(String (250), nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)

class Ship(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String (250))
    url = Column(String (250), nullable=False)
    manufacturer = Column(String (250), nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(String(250), nullable=False)
    passenger = Column(Integer, nullable=False)
    mglt = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey('users.id'))
    entry_id = Column(String(250), ForeignKey('characters.id'), ForeignKey('planets.id'), ForeignKey('ships.id'))


##    what does this function do?
##    def to_dict(self):
##        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
