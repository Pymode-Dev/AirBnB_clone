#!/usr/bin/env python3
import sys

from cmd import Cmd


class Console(Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        """quit - exit the console"""
        sys.exit(0)

    def do_EOF(self, line):
        return True


if __name__ == "__main__":
    Console().cmdloop()
