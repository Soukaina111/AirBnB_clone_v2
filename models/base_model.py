#!/usr/bin/python3
"""This module defines a base class
for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models


Base = declarative_base()


class BaseModel:
    """A base class
    for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates
        a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for clek, NumVal in kwargs.items():
                if clek == "created_at":
                    NumVal = datetime.strptime(NumVal, "%Y-%m-%dT%H:%M:%S.%f")
                if clek == "updated_at":
                    NumVal = datetime.strptime(NumVal, "%Y-%m-%dT%H:%M:%S.%f")
                if clek != "__class__":
                    setattr(self, clek, NumVal)
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()

    def __str__(self):
        """Returns a string
        representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def __repr__(self):
        """ representaion
        """
        return self.__str__()

    def save(self):
        """Updates updated_at with current time
        when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Converts instance
        into a dctnr format"""
        dctnr = self.__dict__.copy()
        dctnr.pop('_sa_instance_state', None)
        dctnr['__class__'] = type(self).__name__
        dctnr['created_at'] = self.created_at.isoformat()
        dctnr['updated_at'] = self.updated_at.isoformat()
        return dctnr

    def delete(self):
        """Deletes the current instance
        from the storage"""
        models.storage.delete(self)
