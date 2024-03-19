#!/usr/bin/python3
"""This module contains the console for the HBNB project."""

import cmd
import sys
import json
from datetime import datetime
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    prompt = "(hbnb) "

    def do_create(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        args = line.split()
        if not args:
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
        all_instances = BaseModel.__objects
        key = "{}.{}".format(class_name, instance_id)
        if key in all_instances:
            print(all_instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        args = line.split()
        if not args:
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
        all_instances = BaseModel.__objects
        key = "{}.{}".format(class_name, instance_id)
        if key in all_instances:
            del all_instances[key]
            BaseModel.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        args = line.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        all_instances = BaseModel.__objects
        if args:
            filtered_instances = [str(v) for k, v in all_instances.items() if k.startswith(args[0])]
        else:
            filtered_instances = [str(v) for v in all_instances.values()]
        print(filtered_instances)

    def do_update(self, line):
        args = line.split()
        if not args:
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
        all_instances = BaseModel.__objects
        key = "{}.{}".format(class_name, instance_id)
        if key not in all_instances:
            print("** no instances found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        try:
            attribute_value = eval(attribute_value)
        except NameError:
            pass

        setattr(all_instances[key], attribute_name, attribute_value)
        all_instances[key].save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
