#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.amenity import Amenity

class DBStorage:
    '''
    This class handles the db engine
    '''
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes DBStorage variables """
        user_name = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user_name}:{password}@{host}/{db}',
            pool_pre_ping=True
        )
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ This method queries objects from
        the db depending
        on the  value of cls"""

        inst = {}

        if cls:
            req = self.__session.query(cls).all()
            for obj in req:
                key = f"{obj.__class__.__name__}.{obj.id}"
                inst[key] = obj
        else:
            Entities = [User, State, City, Amenity, Place, Review]
            for cls in Entities:
                req = self.__session.query(cls).all()
                for obj in req:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    inst[key] = obj

        return inst

    def new(self, obj):
        """ This method adds an obj to db"""
        self.__session.add(obj)

    def save(self):
        """This method saves an obj in db"""
        self.__session.commit()

    def delete(self, obj=None):
        """This method removes an obj is not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ This method Creates all
        tables in the database awith its session's db """
        Base.metadata.create_all(self.__engine)
        factory_se = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory_se)
        self.__session = Session()


    def close(self):
        """Dispose of current session if active"""
        self.__session.remove()
