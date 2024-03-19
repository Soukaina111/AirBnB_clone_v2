#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
import os
from sqlalchemy.orm import relationship, backref
from models.city import City


class State(BaseModel, Base):
    """ State class """
     __tablename__ = "states"
    name = Column(String(128), nullable=False)

    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            city_is = storage.all("City").values()
            return [c for c in city_s if c.state_id == self.id]

