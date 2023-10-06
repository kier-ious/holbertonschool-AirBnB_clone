#!/usr/bin/python3
"""Base Model"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Base class for the console clone"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            k_dict = kwargs.copy()
            del k_dict["__class__"]
            for key in k_dict:
                if (key == "created_at" or key == "updated_at"):
                    k_dict[key] = datetime.strptime(k_dict[key], date_format)
            self.__dfict__ = k_dict

        else:
            """Assigning a unique ID as a string"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Reformating string repr"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updating the update_at attr with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Making a new_dict with extra field for __class__"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.created_at.isoformat()

        return new_dict
