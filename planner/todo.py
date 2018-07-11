import configparser
import os

import requests
from requests.auth import HTTPBasicAuth


class Todo:

    def __init__(self):
        config = configparser.ConfigParser()
        path = os.path.expanduser('~/.planner/config')
        config.read(path)
        self.hostname = config['default']['host']
        user = config['default']['username']
        password = config['default']['password']
        self.auth = HTTPBasicAuth(user, password)

    def list(self):
        url = self.hostname + '/todos/'
        response = requests.get(url, auth=self.auth)
        todos = response.json()
        for todo in todos:
            todo['status'] = 'x' if todo['status'] else 'o'
            print('{status:^3}{id:>3} {text}'.format(**todo))

    def create(self, text, status=''):
        url = self.hostname + '/todos/'
        data = {
            'status': status,
            'text': text}
        response = requests.post(url, auth=self.auth, json=data)
        if response.status_code != 201:
            print('error')

    def patch(self, **data):
        url = self.hostname + '/todos/{id}'.format(id=data['id'])
        response = requests.patch(url, auth=self.auth, json=data)
        if response.status_code != 200:
            print('error')

    def destroy(self, pk):
        url = self.hostname + '/todos/{id}'.format(id=pk)
        data = {'id': pk}
        response = requests.delete(url, auth=self.auth, json=data)
        if response.status_code != 204:
            print('error')
