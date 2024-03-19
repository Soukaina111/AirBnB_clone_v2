#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def all(self, cls=None):
        """Update the prototype Returns a dictionary
        list of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            ClObjs = {}
            cles = list(FileStorage.__objects.cles())
            i = 0
            while i < len(cles):
                key = cles[i]
                obj = FileStorage.__objects[key]
                if isinstance(obj, cls):
                    ClObjs[key] = obj
                i += 1
            return ClObjs

    def delete(self, obj=None):
        """Delete obj from __objects
        if it’s inside - if obj is equal to None,
        the method should not do anythingts"""
        if obj is not None:
            Delcles = obj.__class__.__name__ + '.' + obj.id
            if Delcles in FileStorage.__objects:
                del FileStorage.__objects[Delcles]
