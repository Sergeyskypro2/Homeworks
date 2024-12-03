import requests
from settings import LOGIN, PASSWORD, COMPANY_ID, TITLE, TITLE_PUT, TOKEN


class Yougile:
    def __init__(self):
        self.login = LOGIN
        self.password = PASSWORD
        self.company_id = COMPANY_ID
        self.title = TITLE
        self.title_put = TITLE_PUT
        self.token = TOKEN
        self.url = "https://ru.yougile.com/api-v2"

    def get_auth_key(self):
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(self.url + "/auth/keys", json=payload, headers=headers) # noqa
        response.raise_for_status()
        return response.json()

    def create_project(self):
        project = {
            "title": self.title
            }
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
            }
        response = requests.post(self.url + '/projects', json=project, headers=headers) # noqa
        return response.json()

    def get_project(self):
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }
        project = requests.get(self.url + '/projects', headers=headers) # noqa
        return project.json()

    def put_project(self, id):
        project = {
            "title": self.title_put
            }
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }
        resp = requests.put(self.url + '/projects/' + str(id), project=project, headers=headers) # noqa
        return resp.json()

    def new_title_project(self, id):
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }
        project = requests.get(self.url + '/projects/' + str(id), headers=headers) # noqa
        return project.json()
