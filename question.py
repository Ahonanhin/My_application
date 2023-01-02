from country import *
import pyttsx3
import playsound


from abc import ABC, abstractmethod

class question_archetype(ABC):

    @abstractmethod
    def ask_question(self):
        pass

    @abstractmethod
    def print_reply(self):
        pass

class question (question_archetype):

    _sample_country  =  None
    _inquiry = None
    _answer = None

    def __init__(self, randomCountry):
        self._sample_country = country(randomCountry)

    def print_question(self):
        return self.__inquiry

    def set_answer(self, answer):
        self._answer = answer


class question_1(question):

    def __init__(self, randomCountry):
        super().__init__(randomCountry)
        self._inquiry = "What is the capital of "

    def ask_question(self):
        answer = input(self._inquiry + self._sample_country.get_name() + ": \n")
        self.set_answer(answer)
        return answer
    
    def print_reply(self):
        text_speech = pyttsx3.init()
        text_speech.setProperty("rate", 140)
        if self._answer.lower() == self._sample_country.get_capital().lower():
            text_speech.say("Yes you are right")
        else:
            text_speech.say("No, try again")
        text_speech.runAndWait()


sample = question_1("France")

sample.ask_question()
sample.print_reply()


print("ok")