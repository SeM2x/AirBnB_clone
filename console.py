#!/usr/bin/python3
""" """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "
    
    def __check_class(self, args):
        """
        """
        classes = ['BaseModel']
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
        if not self.__check_class(args):
            return

        model = BaseModel()
        model.save()
        print(model.id)
    
    def do_show(self, arg):
        """
        """
        args = arg.split()

        if not self.__check_class(args):
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in objects.keys():
            print("** no instance found **")
            return

        print(BaseModel(**objects[key]))
    
    def do_destroy(self, arg):
        """
        """
        args = arg.split()
        if not self.__check_class(args):
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in objects.keys():
            print("** no instance found **")
            return

        storage.remove(key)
        storage.save() 

    def do_all(self, arg):
        """
        """
        args = arg.split()
        if not self.__check_class(args):
            return
    
        plist = [BaseModel(**obj).__str__() for obj in storage.all().values()]
        print(plist)
    
    def do_update(self, arg):
        """
        """
        args = arg.split()
        if not self.__check_class(args):
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

        obj[attr] = value
        BaseModel(**obj).save()

    def emptyline(self):
        """
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
