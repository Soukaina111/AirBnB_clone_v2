#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base



class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        InVr = models.storage.all()
        Mylst = []
        rslt = []
        for clek in InVr:
            cty = clek.replace('.', ' ')
            cty = shlex.split(cty)
            if cty[0] == 'City':
                Mylst.append(InVr[clek])
        idx = 0
        while idx < len(Mylst):
            eleitm = Mylst[idx]
            if eleitm.state_id == self.id:
                rslt.append(eleitm)
            idx += 1
        return rslt
