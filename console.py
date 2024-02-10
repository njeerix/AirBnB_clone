#!/usr/bin/python3
"""Console module"""
import cmd
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Command Interpreter class"""
    prompt = "(hbnb) "
    classes = ["BaseModel", {"User": User}, "State", "City", "Amenity", "Place", "Review"]

    def all(self):
        return self.__objects

    def my_errors(self, line, num_args):
        """Checks for errors in the number of arguments"""
        if len(line.split()) < num_args:
            print("** instance id missing **")
            return 1
        return 0

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
        """Prints the string reprresentation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0]
            obj_id = args[1]
            key = class_name + "." + obj_id
            print(storage.all()[key])
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0]
            obj_id = args[1]
            key = class_name + "." + obj_id
            del storage.all()[key]
            storage.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        all_instances = storage.all().values()
        class_instances = [instance for instance in all_instances if instance.__class__.__name__ == class_name]
        print(class_instances)

        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return

        try:
            print([str(obj) for obj in storage.all().values() if obj.__class__.__name__ == arg])
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0]
            obj_id = args[1]
            key = class_name + "." + obj_id
            if key not in storage.all():
                print("** no instance found **")
                return

            obj = storage.all()[key]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 3:
                print("** value missing **")
                return

            attribute_name = args[2]
            attribute_value = args[3]
            
            setattr(obj, attribute_name, attribute_value)
            obj.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def emptyline(self):
        pass

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        count = len([instance for instance in storage.all().values() if instance.__class__.__name__ == class_name])
        print(count)

if __name__ == '__main__':
    cli = HBNBCommand()
    cli.cmdloop()
