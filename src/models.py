import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
   



class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table planetas.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre_planeta = Column(String(250))
    descripcion = Column(String(250))


class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table personajes.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre_personaje = Column(String(250))
    descripcion = Column(String(250))
 

class PersonajesFavoritos(Base):
    __tablename__ = 'personajes favoritos'
    # Here we define columns for the table personajes favoritos.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre_personaje = Column(String(250))
    descripcion = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    Personajes_id = Column(Integer, ForeignKey('personajes.id'))
    Personajes = relationship(Personajes)

    
class PlanetasFavoritos(Base):
    __tablename__ = 'planetas favoritos'
    # Here we define columns for the table planetas favoritos.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre_planeta = Column(String(250))
    descripcion = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship(Planetas)











    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
