#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy import Column, String


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    text = Column("text", String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
