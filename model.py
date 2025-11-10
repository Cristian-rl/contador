from abc import ABC, abstractmethod

class ContadorBase(ABC):
    @abstractmethod
    def contar(self, texto):
        pass

class ContadorCaracteres(ContadorBase):
    def contar(self, texto):
        return len(texto)
