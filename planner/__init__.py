import cmd
import configparser
import os

from .todo import Todo


class PlannerCmd(cmd.Cmd):

    def __init__(self):
        config = configparser.ConfigParser()
        path = os.path.expanduser('~/.planner/config')
        config.read(path)
        hostname = config['default']['host']
        user = config['default']['username']
        password = config['default']['password']
        self.todo = Todo(hostname, user, password)
        super().__init__()

    def do_todo(self, args):
        if args == 'list':
            todos = self..todo.list()
            for todo in todos:
                if not todo['status']:
                    todo['status'] = 'o'
                print('{status:^3}{id:>3} {text}'.format(**todo))
        if args == 'add':
            self.todo.add('hello')

    def do_exit(self, arg):
        return True
