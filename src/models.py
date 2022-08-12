import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False) 
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
   
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url =  Column(String(250), nullable=False) 
    post_id = Column(Integer, ForeignKey('post.id'))


class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey('user.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')