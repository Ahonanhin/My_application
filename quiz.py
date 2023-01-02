
from abc import ABC, abstractmethod
import random
from firebase import trav
import pyttsx3


from country import *
class quiz_contract():
    pass

class quiz():
    _answer = None
    _propositions = []
    _question = None

    def __init__(self) -> None:
        pass
    
    def display_question(self):
        # text_speech = pyttsx3.init()
        # text_speech.setProperty("rate", 140)
        for i in range (0, len(self._propositions)):
            print (str(i+1) + ". " + self._propositions[i]) 
        #     text_speech.say(str(i+1) + ". " + self._propositions[i])
        # text_speech.say(self._question)
        # print(self._question)
        # text_speech.runAndWait()

    def check_answer(self):
        # text_speech = pyttsx3.init()
        # text_speech.setProperty("rate", 140)
        
        answer_choice = input(self._question + ":\n")
        if len(answer_choice) == 1:
            answer_choice = int(answer_choice)
        
        if isinstance(answer_choice, int):
            if int(answer_choice) > 4:
                return 0
            if self._propositions[answer_choice - 1] == self._answer.get_capital():
                print("Great Job")
                # text_speech.say("Great Job")
                # text_speech.runAndWait()
                return 1
            else:
                print(self._propositions[answer_choice])
                print(" Sorry, not right this time")
                # text_speech.say("Sorry, not right this time")

        else:
            if answer_choice == self._answer.get_capital():
                print("Great Job")
                # text_speech.say("Great Job")
                # text_speech.runAndWait()
                return 1
            else:
                print("Sorry, not right this time")
        #         text_speech.say("Sorry, not right this time")
        # text_speech.runAndWait()
        return 0

class quiz_capital(quiz):
    _pos_ = None
    def __init__(self) -> None:
        self._propositions = []
        num = random.randint(0,249)
        self._answer = country(trav.child(str(num)).child("countryName").get())

        l = list(range(0,num)) +list(range(num + 1, 249))

        for i in range(0,3):
            self._propositions.append(trav.child(str(random.choice(l))).child("capital").get())
        
        self._propositions.append(self._answer.get_capital())

        random.shuffle(self._propositions)

        self._question = "What is the capital of " + self._answer.get_name()


    def __init__(self, a) -> None:
        self._propositions = []
        num = random.randint(0,249)
        self._pos_ = num
        self._answer = country(trav.child(str(num)).child("countryName").get())

        l = list(range(0,num)) +list(range(num + 1, 249))

        for num in a:
            if num in l:
                l.remove(num)

        for i in range(0,3):
            self._propositions.append(trav.child(str(random.choice(l))).child("capital").get())
        
        self._propositions.append(self._answer.get_capital())

        random.shuffle(self._propositions)

        self._question = "What is the capital of " + self._answer.get_name()
    
    
        
