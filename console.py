#!/usr/bin/python3
"""Console module"""
import cmd
from models import storage
from models.base_model import BaseModel
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    """Command Interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string reprresentation of an insatnce"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = arg.split()
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            key = class_name + "." + instance_id
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = arg.split()
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            key = class_name + "." + instance_id
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instance"""
        if not arg:
            print([str(value) for key, value in storage.all().items() if isinstance(value, BaseModel)])
        else:
            try:
                if arg not in storage.classes():
                    print("** class doesn't exist **")
                    return
                print([str(value) for key, value in storage.all().items() if arg in key])
            except ValueError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + "." + instance_id
            if key not in storage.all():
                print("** no instance name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            value = args[3]
            instance = storage.all()[key]
            setattr(instance, attribute_name, value)
            instance.updated_at = datetime.now()
            storage.save()

        except ValueError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
