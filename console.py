#!/usr/bin/python3
"""This module contains the entry point of the command interpreter."""
import cmd
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb) "
    classes = {
        "BaseModel": models.BaseModel,
        "User": models.User,
        "State": models.State,
        "City": models.City,
        "Amenity": models.Amenity,
        "Place": models.Place,
        "Review": models.Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of a specified class."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        args = ' '.join(args[1:])
        kwargs = {}
        for pair in args.split(","):
            pair = pair.strip()
            if "=" in pair:
                key, value = pair.split("=")
                key = key.strip()
                value = value.strip()
                if value.startswith('"') and value.endswith('"'):
                    # Remove quotes and replace underscores with spaces
                    value = value[1:-1].replace('_', ' ')
                    kwargs[key] = value
                elif "." in value:
                    try:
                        kwargs[key] = float(value)
                    except ValueError:
                        print("** invalid value for float parameter {} **".format(key))
                elif value.isdigit():
                    kwargs[key] = int(value)
                else:
                    print("** invalid value for parameter {} **".format(key))
            else:
                print("** invalid syntax for parameter **")
                return
        new_instance = self.classes[class_name](**kwargs)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        key = class_name + '.' + args[1]
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        key = class_name + '.' + args[1]
        if key in objs:
            del objs[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if not arg:
            objs = models.storage.all()
            print([str(objs[key]) for key in objs])
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        objs = models.storage.all(class_name)
        print([str(obj) for obj in objs.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = class_name + '.' + args[1]
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objs[key], args[2], args[3].replace('"', ''))
        models.storage.save()

    def do_count(self, arg):
        """Count instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        objs = models.storage.all(arg)
        print(len(objs))

    def default(self, arg):
        """Called on an input line when the command prefix is not recognized"""
        args = arg.split('.')
        if len(args) < 2 or args[1] != "all()":
            print("** Unknown syntax: {}".format(arg))
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        objs = models.storage.all(class_name)
        print([str(obj) for obj in objs.values()])

if __name__ == "__main__":
    HBNBCommand().cmdloop()
