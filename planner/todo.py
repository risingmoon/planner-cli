import requests
from requests.auth import HTTPBasicAuth


class Todo:

    def __init__(self, hostname, user, password):
        self.auth = HTTPBasicAuth(user, password)
        self.url = hostname + '/todos/'

    def list(self):
        response = requests.get(self.url, auth=self.auth)
        todo_list = response.json()
        return todo_list

    def add(self, text, status=''):
        data = {
            'status': status,
            'text': text}
        response = requests.post(self.url, auth=self.auth, json=data)
        print(response.json())
