#!/usr/bin/python3
"""entry point of command interpreter"""
import cmd
import json
import os
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """prompts user for input"""
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """use Ctrl+D to exit program"""
        print()
        return True

    def emptyline(self):
        """Do nothing if empty line"""
        pass

    def do_create(self, arg):
        """creates new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.strip()
            if class_name in self.classes:
                # Instantiate object of specified class
                new_instance = globals()[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """prints string rep of instance of BaseModel"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        objects = FileStorage().all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """destroys instance of BaseModel"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id

        objects = FileStorage().all()
        if key in objects:
            del objects[key]
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """prints string rep of all instances of BaseModel"""
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        objects = FileStorage().all()

        filtered_objects = {}
        for key, value in objects.items():
            if value.__class__.__name__ == arg:
                filtered_objects[key] = value

        for instance in filtered_objects.values():
            instance_string = instance.to_dict()
            print(instance_string)

    def do_update(self, arg):
        """updates instance of BaseModel"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id

        objects = FileStorage().all()
        if key in objects:
            if len(args) < 3:
                print("** attribute name missing **")
            if len(args) < 4:
                print("** value missing **")
                return

            attr_name = args[2]
            attr_value = args[3]

            obj = objects[key]
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
