import json
import os.path
from abc import ABC
from abc import abstractmethod


class FileService(ABC):
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def read_from_file(self):
        pass

    @abstractmethod
    def write_to_file(self, data):
        pass

    @property
    def file_address(self):
        return os.path.join('.', 'search_history', self.file_name)

    def file_exists(self):
        return os.path.exists(self.file_address)


class JSONService(FileService):

    def read_from_file(self):
        if self.file_exists():
            with open(self.file_address, 'r', encoding='utf8') as file:
                result = json.load(file)
            return result
        return None

    def write_to_file(self, data):
        with open(self.file_address, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)
