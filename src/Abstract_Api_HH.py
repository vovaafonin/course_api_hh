from abc import ABC, abstractmethod


class AbstractApiHH(ABC):
    @abstractmethod
    def get_vacancy(self, name_vacancy):
        pass
