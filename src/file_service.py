import json
import os.path
from abc import ABC
from abc import abstractmethod


class FileService(ABC):
    def __init__(self, file_address):
        self.file_address = file_address

    @abstractmethod
    def read_from_file(self):
        pass

    @abstractmethod
    def write_to_file(self, data):
        pass

    def file_exists(self):
        return os.path.exists(self.file_address)


class JSONService(FileService):

    def read_from_file(self):
        if self.file_exists():
            with open(self.file_address, 'r') as file:
                result = json.load(file)
            return result
        return None

    def write_to_file(self, data):
        with open(self.file_address, 'w') as file:
            json.dump(file, data)
