from my_interface import MyInterface

class ClassOne(MyInterface):

    def __init__(self) -> None:
        self._url = 'http://localhost'

    def method_one(self, param: dict) -> dict:
        """Method One"""
        print('Method One Implemented!')
        return {'success': 'Method One'}

    def method_two(self, param: dict) -> dict:
        """Method Two"""
        print('Method Two Implemented!')
        return {'success': 'Method Two'}

    @property
    def url(self) -> str:
        """Method URL"""
        #print('Method URL Implemented!')
        return self._url