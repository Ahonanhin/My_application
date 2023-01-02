from quiz import *

class game():
    __attempts__ = None
    __correct__ = None
    __question__ = None
    __temp__ = []

    def __init__(self) -> None:
        self.__attempts__ = 0
        self.__correct__ = 0

    def display_score(self):
        print ("You have ", self.__correct__, "out of 10")

    def play(self):
        while(self.__attempts__ < 11):
            self.__question__ = quiz_capital(self.__temp__)
            self.__temp__.append(self.__question__._pos_)
            self.__question__.display_question()
            self.__correct__ += self.__question__.check_answer()
            self.__attempts__ += 1
            self.__question__ = None
        
        self.display_score()
    
        
test = game()

test.play()