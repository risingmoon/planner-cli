import argparse
import cmd

from .todo import Todo


class TodoCmd(cmd.Cmd):

    def __init__(self):
        self.todo = Todo()
        super().__init__()

    def do_list(self, args):
        self.todo.list()

    def do_add(self, args):
        self.todo.create(text=args)

    def do_edit(self, arg):
        parser = argparse.ArgumentParser()
        parser.add_argument('pk', type=int)
        parser.add_argument(
            'text', type=str, nargs='*',
            help="this is a string")
        parser.add_argument(
            '--status',
            choices=['', 'completed'],
            help="this is a string")
        args = parser.parse_args(arg.split())
        data = {'id': args.pk}
        if args.text:
            data['text'] = ' '.join(args.text)
        if args.status:
            status = {'completed': 'CMP'}
            data['status'] = status[args.status]
        self.todo.patch(**data)

    def do_check(self, arg):
        pass

    def do_rm(self, arg):
        self.todo.destroy(int(arg))

    def do_exit(self, arg):
        return True
