from turtle import title
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Book(Base):
	__tablename__ = 'book'
	id = Column('id', Integer, primary_key=True, index=True)
	title = Column(String)
	rating = Column(Integer)
	timeCreated = Column(DateTime(timezone=True), server_default=func.now())
	timeUpdated = Column(DateTime(timezone=True), onupdate=func.now())
	author_id = Column(Integer, ForeignKey('author.id'))

	author = relationship('Author')

class Author():
	__tablename__ = 'author'
	id = Column('id', Integer, primary_key=True)
	name = Column(String)
	age = Column(Integer)
	timeCreated = Column(DateTime(timezone=True), server_default=func.now())
	timeUpdated = Column(DateTime(timezone=True), onupdate=func.now())

