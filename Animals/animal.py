import random

class Animal:
    #Indicate the animal’s type
    __animal_type = ''
    #Indicate the animal's mode
    __mood = ''
    #Indicate the animal's name
    __name = ''
    #the method of "__init__" of class
    def __init__(self,animal_type,animal_name):
        self.__animal_type = animal_type
        self.__name = animal_name
        #Generate a random number between 1 and 3.
        x=random.randrange(1,4)   
        if x==1:
            self.__mood = 'happy'
        elif x==2:
            self.__mood = 'hungry'
        else:
            self.__mood = 'sleepy'
    #should return the value of the __animal_type field.
    def get_animal_type(self):
        return self.__animal_type
    #should return the value of the __name field.
    def get_name(self):
        return self.__name
    #should return the value of the __mood field.
    def check_mood(self):
        return self.__mood

