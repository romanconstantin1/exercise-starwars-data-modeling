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

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    entry_name = Column(String (250), ForeignKey('users.id'))
    fetch_link = Column(String (250), nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    char_name = Column(String (250), ForeignKey('entries.fetch_link'))
    char_height = Column(Integer, nullable=False)
    char_mass = Column(Integer, nullable=False)
    char_hair_color = Column(String (250))
    char_skin_color = Column(String (250), nullable=False)
    char_eye_color = Column(String (250), nullable=False)
    char_birth_year = Column(String (250), nullable=False)
    char_gender = Column(String (250))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String (250), ForeignKey('entries.fetch_link'))
    planet_diameter = Column(Integer, nullable=False)
    planet_gravity = Column(String(250), nullable=False)
    planet_population = Column(String(250), nullable=False)
    planet_climate = Column(String(250), nullable=False)
    planet_terrain = Column(String(250), nullable=False)

class Ship(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    ship_name = Column(String (250), ForeignKey('entries.fetch_link'))
    ship_manufacturer = Column(String (250), nullable=False)
    ship_length = Column(Integer, nullable=False)
    ship_crew = Column(String(250), nullable=False)
    ship_passenger = Column(Integer, nullable=False)
    ship_mglt = Column(Integer, nullable=False)
    ship_consumables = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorite_name = Column(String(250))
    single_view_link = Column(String(250), ForeignKey('users.id'))


##    what does this function do?
##    def to_dict(self):
##        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
