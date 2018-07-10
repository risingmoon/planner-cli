import cmd
import configparser
import os

import requests
from requests.auth import HTTPBasicAuth


class PlannerCmd(cmd.Cmd):

    def __init__(self):
        config = configparser.ConfigParser()
        path = os.path.expanduser('~/.planner/config')
        config.read(path)
        self.hostname = config['default']['host']
        user = config['default']['username']
        password = config['default']['password']
        self.auth = HTTPBasicAuth(user, password)
        super().__init__()

    def do_task(self, arg):
        import pdb; pdb.set_trace()
        url = self.hostname + '/tasks'
        if arg == 'list':
            response = requests.get(url, auth=self.auth)
            print(response.json())
        if arg == 'add':
            response = requests.get(url, auth=self.auth)

    def do_exit(self, arg):
        return True
