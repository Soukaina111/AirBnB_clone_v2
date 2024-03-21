#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Integer, ForeignKey
from sqlalchemy import Column, String


class Review(BaseModel):
    """ Review classto store review information """
 

    text = Column("text", String(1024), nullable=False)
