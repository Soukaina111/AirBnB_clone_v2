#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initializes a new State instance """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.cities = relationship('City', cascade='all, delete', backref='state')
        else:
            @property
            def cities(self):
                '''
                Returns a list of City instances with
                state_id = State.id.
                '''

                c_dict = models.storage.all(City)
                return [city for city in c_dict.values()
                        if city.state_id == self.id]

