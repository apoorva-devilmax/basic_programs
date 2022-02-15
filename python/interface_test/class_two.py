from my_interface import MyInterface

class ClassTwo(MyInterface):
    def method_one(self, param: dict) -> dict:
        """Method One"""
        print('Method One Implemented!')
        return {'success': 'Method One'}

    def method_three(self, param: dict) -> dict:
        """Method Three"""
        print('Method Three Implemented!')
        return {'success': 'Method Three'}