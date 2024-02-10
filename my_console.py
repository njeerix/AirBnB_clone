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
                self.print_help()
            else:
                print("Unknown command. Type 'help' for assistance.")
    def print_help(self):
        """
        Print help information.
        """

        print("Documented commands commands (type help <topic):")
        print("================================================")
        print("EOF help quit")

    def run_script(self, script_file):
        """
        Run commands from a script file.
        """
        with open(script_file, 'r') as file:
            for line in file:
                self.onecmd(line.strip())

    def onecmd(self, line):
        """
        Process a single command.
        """
        if line == "quit":
            return True
        elif line == "help":
            self.print_help()
        else:
            print("Unknown command:", line)


if __name__ == "__main__":
    console = Console()
    if len(sys.argv) > 1:
        script_file = sys.argv[1]
        console.run_script(script_file)
    else:
        console.cmdloop()
