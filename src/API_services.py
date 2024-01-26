import json
from abc import ABC
from abc import abstractmethod

import requests

SUPERJOBS_SECRET_KEY = 'v3.r.138123228.fcad2a7899a2e09e59c6796790792ee0de4a63db.5808c31acf896ca0c0b1ef647bdde2a99172e66d'


class APIService(ABC):

    def __init__(self, request):
        self.request = request

    @abstractmethod
    def API_request(self):
        pass


class HeadHunterAPI(APIService):

    def API_request(self):
        params = {'text': self.request}
        response = requests.get(url='https://api.hh.ru/vacancies', params=params)
        return response.json()


class SuperJobAPI(APIService):

    def API_request(self):
        headers = {'X-Api-App-Id': SUPERJOBS_SECRET_KEY}
        request_params = {'keyword': self.request}
        vacancies = (requests
                     .get('https://api.superjob.ru/2.0/vacancies/', params=request_params, headers=headers)
                     .json())
        return vacancies


with open('new_file_sj.json', 'w', encoding='utf8') as file:
    api = SuperJobAPI('python')
    json.dump(api.API_request()['objects'], file,ensure_ascii=False)
with open('new_file_hh.json', 'w', encoding='utf8') as file:
    api = HeadHunterAPI('python')
    json.dump(api.API_request()['items'], file, ensure_ascii=False)
# print(SuperJobAPI('python').API_request()['objects'])
# print(HeadHunterAPI('python').API_request()['items'])
