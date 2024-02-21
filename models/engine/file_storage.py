#!/usr/bin/python3
"""This is the file storage module for the AirBnB project."""
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
    """This class manages serialization of instances to a JSON file and
    deserialization of JSON file to instances.
    Attributes:
        __file_path: A string representing the path to the JSON file.
        __objects: A dictionary containing objects stored by their unique IDs.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary or objects of a specified class.
        Args:
            cls (class, optional): The class type to filter objects.
        Returns:
            dict: A dictionary of objects or objects filtered by class.
        """
        obj_dict = {}
        if cls:
            obj_dict = {
                key: obj
                for key, obj in self.__objects.items()
                if isinstance(obj, cls)
            }
        else:
            obj_dict = self.__objects
        return obj_dict

    def new(self, obj):
        """Adds a new object to __objects.
        Args:
            obj: The object to be added.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects and saves to the JSON file."""
        serializable_objs = {
            key: obj.to_dict() for key, obj in self.__objects.items()
        }
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(serializable_objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                deserialized_objs = json.load(f)
                for key, value in deserialized_objs.items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects if it exists.
        Args:
            obj: The object to be deleted.
        """
