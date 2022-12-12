import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    Username = Column(String(250))
    Name = Column(String(250))
    Lastname = Column(String(250))
    Password = Column(String(250))


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    Video_Photo = Column(String(250)) 
    Description = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))        
    user = relationship(User)

class Follower(Base):
    __tablename__= 'follower'
    id = Column(Integer, primary_key=True)
    Username = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))        
    user = relationship(User)

class Suggestions(Base):
    __tablename__='suggestions'
    id = Column(Integer, primary_key=True) 
    Username = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))        
    user = relationship(User)


class Likes(Base):
    __tablename__='likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))        
    user = relationship(User)
    media_id = Column(Integer, ForeignKey('media.id'))
    media = relationship('Media')


class Saved(Base):
    __tablename__= 'saved'
    id = Column(Integer, primary_key=True)
    Video_Photo = Column(String(250)) 
    user_id = Column(Integer, ForeignKey('user.id'))        
    user = relationship(User)
    media_id = Column(Integer, ForeignKey('media.id'))
    media = relationship(Media)


class Comments(Base):
    __tablename__='comments'
    id = Column(Integer, primary_key=True)  
    media_id = Column(Integer, ForeignKey('media.id'))
    media = relationship(Media)
    user_id = Column(Integer, ForeignKey('user.id'))        
    user = relationship(User)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e


