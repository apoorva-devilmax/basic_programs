import abc

class MyInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'method_one') and 
                callable(subclass.method_one) and 
                hasattr(subclass, 'method_two') and 
                callable(subclass.method_two) or 
                NotImplemented)

    @abc.abstractmethod
    def method_one(self, param: dict) -> dict:
        """Method One"""
        raise NotImplementedError

    @abc.abstractmethod
    def method_two(self, param: dict) -> dict:
        """Method Two"""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def url(self) -> str:
        raise NotImplementedError