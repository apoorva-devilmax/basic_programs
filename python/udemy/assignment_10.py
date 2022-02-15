# import core modules
from abc import abstractmethod, ABC


class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):

    def scroll(self):
        print("HP Scroll")


class DELL(TouchScreenLaptop):

    def scroll(self):
        print("Dell Scroll")


class HPNotebook(HP):

    def click(self):
        print("HP Notebook Click")


class DELLNotebook(HP):

    def click(self):
        print("Dell Notebook Click")


# tsl = TouchScreenLaptop() # Can't instantiate
# hp = HP() # Can't instantiate
# dl = DELL() # Can't instantiate
hpnote = HPNotebook()
hpnote.scroll()
hpnote.click()

dlnote = DELLNotebook()
dlnote.scroll()
dlnote.click()