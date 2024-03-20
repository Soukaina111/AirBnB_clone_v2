#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
import os
from models import storage


class Place(BaseModel, Base):
    """ A place to stay 
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []"""

    __tablename__ = 'places'
    
    type_storage = os.getenv("HBNB_TYPE_STORAGE")

    if type_storage == "db":
        reviews = relationship('Review', cascade='all, delete', backref='place', passive_deletes=True)
    else:
        @property
        def reviews(self):
            """ This is a getter attribute for reviews module """
            list_r = []
            for rev in storage.all("Review").values():
                if rev.place_id == self.id:
                    list_r.append(rev)
            return list_r


    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
