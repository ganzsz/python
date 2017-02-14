mport abc
from abstractie import BaseClass

class Implementatie(BaseClass):
    def hen(self, poep):
        return

obj = Implementatie()
obj.hennie()
print (issubclass(Implementatie, BaseClass))