from firebase import *
import random
class country:

    __name = None
    __population = None
    __capital = None
    __continent = None
    __currency = None

    # def __new__(cls):
    #     print("Creating new empty class")
    #     return super().__new__(cls)
        

    def __init__(self, name):
        # trav = ref.reference("/countries/country")
        for country in trav.get():
            if country["countryName"] == name:
                self.__name = name
                self.__continent = country["continentName"]
                self.__population = int(country["population"])
                self.__capital = country["capital"]

    # @classmethod
    # def randomizer(self):
    #     num  = random.randint(0,249)
    #     self.__name = trav.chil(
        


    #getters
    def get_name(self):
        return self.__name

    def get_continent(self):
        return self.__continent

    def get_population(self):
        return self.__population
    
    def get_capital(self):
        return self.__capital

    def get_currency(self):
        return self.__currency