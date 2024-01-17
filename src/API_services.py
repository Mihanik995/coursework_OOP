from abc import ABC
from abc import abstractmethod


class APIService(ABC):

    @abstractmethod
    def API_request(self):
        pass
