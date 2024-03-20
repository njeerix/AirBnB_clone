#!/usr/bin/python3
"""This module contains the console for the HBNB project."""

import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show string represenation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objs = models.storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exists **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objs = models.storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances."""
        args = arg.split()
        all_objs = models.storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in all_objs.values()
              if type(obj).__name__ == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objs = models.storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(all_objs[key], args[2], args[3])
        models.storage.save()

    def do_count(self, arg):
        """Count the number of instances of a class."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for obj in models.storage.all().values()
                    if type(obj).__name__ == args[0])
        print(count)

    def do_User_all(self, arg):
        """Retrieve all instances of User."""
        self.do_all("User")

    def do_State_all(self, arg):
        """Retrieve all instances of State."""
        self.do_all("State")

    def do_City_all(self, arg):
        """Retrieve all instances of City."""
        self.do_all("City")

    def do_Amenity_all(self, arg):
        """Retrieve all instances of Amenity."""
        self.do_all("Amenity")

    def do_Place_all(self, arg):
        """Retrieve all instances of Place."""
        self.do_all("Place")

    def do_Review_all(self, arg):
        """Retrieve all instances of Review."""
        self.do_all("Review")

    def do_User_count(self, arg):
        """Count the number of instances of User."""
        self.do_count("User")

    def do_City_count(self, arg):
        """Count the number of instances of City."""
        self.do_count("City")

    def do_Amenity_count(self, arg):
        """Count the number of instances of Amenity."""
        self.do_count("Amenity")

    def do_Place_count(self, arg):
        """Count the number of instances of Place."""
        self.do_count("Place")

    def do_User_show(self, arg):
        """Show details of a specific User instance."""
        self.do_show("User" + arg)

    def do_User_destroy(self, arg):
        """Destroy a specific User interface."""
        self.do_destroy("User" + arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
