#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
import models
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            '''
            Returns a list of City instances with state_id equal to the current State.id.
            '''

            c_dict = models.storage.all(City)
            return [city for city in c_dict.values() if city.state_id == self.id]
