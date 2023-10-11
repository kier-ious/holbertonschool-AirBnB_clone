#!/usr/bin/python3
"""FileStorage that serializes to a JSON file and deserializes
files to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict __objects"""
        return (self.__objects)

    def new(self, obj):
        """Sets in __objects the obj w/ key <obj class name>.id"""
        if obj:
            key = obj.__class__.__name__ + "." + str(obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as json_path:
            json.dump(serialized_objects, json_path)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        class_mapping = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        try:
            with open(self.__file_path, 'r') as f:
                # Iterate through JSON data
                for key, value in json.load(f).items():

                    # Get class name from object's dictionary
                    obj_class_name = value.get("__class__")

                    if obj_class_name in class_mapping:
                        del value["__class__"]
                        obj_class = class_mapping[obj_class_name]
                        try:
                            # Create instance of class using object data
                            obj = obj_class(**value)
                            # Store instance in file system
                            self.new(obj)
                        except Exception as e:
                            print(f"Error loading data from JSON: {e}")
        except FileNotFoundError:
            pass
