#!/usr/bin/python3

""" File storage class for AirBnB"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:

    """
    Serializes instances to a JSON &
    deserializes JSON to instances

    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):

        """

        returns a dict
        Return:
            returns a dict of __object
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):

        """ sets new json object

        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):

        """ for saving as JSON """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):

        """ serializes file path to JSON """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value

        except FileNotFoundError:
            pass

    def delete(self, obj=None):

        """ deletion by key """

        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):

        """ calls reload() to refresh """
        self.reload()
