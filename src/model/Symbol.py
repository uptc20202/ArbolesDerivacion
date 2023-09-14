from abc import ABC, abstractmethod

class Symbol(ABC):
    @abstractmethod
    def get_path_image(self):
        pass

    @abstractmethod
    def get_symbol(self):
        pass
