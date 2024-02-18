from abc import ABC, abstractmethod


class AbstractJson(ABC):

    @abstractmethod
    def file_save(self, data: list):
        pass

    @abstractmethod
    def file_read(self):
        pass
