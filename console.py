#!/usr/bin/python3
""" """
import cmd


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "
    
    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True
    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
