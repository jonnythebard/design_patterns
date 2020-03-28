"""
Don't put too much into an interface; split into separate interface.
YAGNI - You Ain't Going to Need It
"""
import abc


class Machine:
    """
    interface with too many abstract function isn't good.
    """
    @abc.abstractmethod
    def print(self, document):
        raise NotImplemented

    @abc.abstractmethod
    def fax(self, document):
        raise NotImplemented

    @abc.abstractmethod
    def scan(self, document):
        raise NotImplemented


class MultiFunctionPrinter(Machine):
    """
    In multi function printer, print, fax, scan is all implemented.
    using Machine interface is no problem.
    """
    def print(self, document):
        """Do something"""
        pass

    def fax(self, document):
        """Do something"""
        pass

    def scan(self, document):
        """Do something"""
        pass


class OldFashionedPrinter(Machine):
    """
    In old fashioned printer, only print is implemented.
    Machine interface isn't good.
    """
    def print(self, document):
        """Do something"""
        pass


"""
It is better to separate interfaces.
"""


class Printer:
    @abc.abstractmethod
    def print(self, document):
        raise NotImplemented


class Scanner:
    @abc.abstractmethod
    def scan(self, document):
        raise NotImplemented


class MyPrinter(Printer):
    @abc.abstractmethod
    def print(self, document):
        """Do something"""
        pass


class PhotoPrinter(Printer, Scanner):
    def print(self, document):
        """Do something"""
        pass

    def scan(self, document):
        """Do something"""
        pass
