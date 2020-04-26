#!/usr/bin/python3
"""Basic CLI in Python3"""

import threading as th
import time

cont=True
text=None

class InputThread:
    def __init__(self):
        global cont
        global text
        while True:
            self.loop_thread()
            time.sleep(1)
            text=None
            cont=True

    def loop_thread(self):
        global cont
        global text
        text = input()
        cont=False


class CLI:
    def __init__(self):
        self.cmds = {
            'help':self.help,
            }
        self.init_message = ''

    def help(self, args=None):
        """Use help 'command' for more information on a specific command."""
        if args==None:
            print("Available Commands:")
            for key in self.cmds.keys():
                print(key)
            print(self.help.__doc__)

        else:
            print(self.cmds[args[0]].__doc__)

    def set_message(self, message):
        """Sets the initialization message"""
        self.init_message = message

    def add_function(self, name, function):
        """Adds a function to the command dictionary"""
        self.cmds[name] = function
        
    def cli(self, a):
        global cont
        args = a.split(' ')
        if args[0] not in self.cmds.keys():
            print('Command "', args[0], '" Not Found.')
            self.help()
        else:
            if len(args) == 1:
                self.cmds[args[0]]()
            else:
                self.cmds[args[0]](args[1:])
        cont=True
        
    def loop(self):
        global cont
        global text
        print(self.init_message)
        th.Thread(target=InputThread, args=(), name='user_input_thread', daemon=True).start()
        while True:
            if not cont:
                self.cli(text)

if __name__ in '__main__':
    x = CLI().loop()
