#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Integer, ForeignKey
from sqlalchemy import Column, String


class Review(BaseModel):
    """ Review classto store review information """
 
    __tablename__ = 'reviews'

    text = Column("text", String(1024), nullable=False)
