#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
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
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __unique_file_path: path to the JSON file
        __unique_objects: objects will be stored
    """
    __unique_file_path = "unique_file.json"
    __unique_objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __unique_objects
        """
        unique_dict = {}
        if cls:
            objects_dict = self.__unique_objects
            for key in objects_dict:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    unique_dict[key] = self.__unique_objects[key]
            return (unique_dict)
        else:
            return self.__unique_objects

    def new(self, obj):
        """sets __unique_objects to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__unique_objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__unique_objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__unique_file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__unique_file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__unique_objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__unique_objects[key]

    def close(self):
        """ calls reload()
        """
        self.reload()
