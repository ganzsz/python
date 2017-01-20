import abc

class BaseClass(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def hennie(self):
        print(self.__class__.__name__)
        return