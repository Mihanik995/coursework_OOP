from abc import ABC
from abc import abstractmethod
import requests


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
        pass
