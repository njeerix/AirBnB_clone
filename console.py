#!/usr/bin/python3
"""This module contains the console for the HBNB project."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseMode;
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i  in lexer]
            retl.append(brackets.group())
            return retl


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg;[0])().id)
            storage.save()

    def do_show(self, arg):
        """Show string represenation of an instance."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arg;[0], argl[1])]
            storage.save()

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
    file_path = 'file.json'
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass


    HBNBCommand().cmdloop()
