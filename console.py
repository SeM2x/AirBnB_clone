#!/usr/bin/python3
""" """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "

    def __class_exists(self, args):
        """
        """
        classes = [
                'BaseModel',
                'User',
                'State',
                'City',
                'Amenity',
                'Place',
                'Review'
                ]
        if not args:
            print("** class name missing **")
            return False

        if args[0] not in classes:
            print("** class doesn't exist **")
            return False

        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_create(self, arg):
        """
        """
        args = arg.split()
        if not self.__class_exists(args):
            return

        Class = globals()[args[0]]
        obj = Class()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        """
        args = arg.split()

        if not self.__class_exists(args):
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in objects.keys():
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        """
        """
        args = arg.split()
        if not self.__class_exists(args):
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in objects.keys():
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, arg):
        """
        """
        args = arg.split()
        if not self.__class_exists(args):
            return

        Class = globals()[args[0]]
        obj_list = [str(obj) for obj in storage.all().values()
                    if obj.to_dict()['__class__'] == args[0]]
        print(obj_list)

    def do_update(self, arg):
        """
        """
        args = arg.split()
        if not self.__class_exists(args):
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in objects.keys():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        value = args[3]
        obj = objects[key]
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                value = value.replace('"', '')

        obj.__dict__[attr] = value
        obj.save()

    def emptyline(self):
        """
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
