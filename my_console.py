#!/usr/bin/python3

class MyClass:
    def add(self, x, y):
        return x + y
"""
AirBnB Clone - Console Module
"""

import sys


class Console:
    """
    The console class for managing AirBnB objects.
    """

    def __init__(self):
        """
        Initialize the Console instance.
        """
        self.prompt = "(hbnb) "
        
    def cmdloop(self):
        """
        Run the command loop.
        """
        while True:
            user_input = input(self.prompt)
            if user_input == "quit":
                break
            elif user_input == "help":
                print("Documented commands commands (type help <topic):")
                print("================================================")
                print("EOF help quit")
            else:
                print("Unknown command. Type 'help' for assistance.")

if __name__ == "__main__":
    console = Console()
    if len(sys.argv) > 1:
        with open(sys.arg[1], 'r') as script_file:
            for line in script_file:
                console.onecmd(line.strip())
    else:
        console.cmdloop()
