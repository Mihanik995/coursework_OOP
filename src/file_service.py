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
