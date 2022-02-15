from getpass import getpass

class InvalidPasswordException(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg

try:
    pswd = getpass("Please enter a password: ")
    if len(pswd) < 8:
        raise InvalidPasswordException("Password length should be minimum of 8 chars.")
    else:
        print("Password is okay")
except InvalidPasswordException as ex:
    print(ex)
