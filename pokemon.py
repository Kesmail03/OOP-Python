import string
import numpy as np
#Khaled Esmail,cs302,Karla Fant


#hierarchy classes based and derived


#Base character class
class Character(): 
    def __init__(self):
        self._name = self.insert()
        self._history = self.description()

    def insert(self):    
        #exception handling
        try:
            return str(input("Please enter the name: "))

        except ValueError:
            print("Invalid info entered")

    def description(self):
        #exception handling
        try: 
            self._history = input("Please enter the history: ")

        except ValueError:
            print("Invalid info")

    def display(self):
        print("The name is: ",self._name)

    def display_history(self):
        print("The history is: ",self._history)

    def __lt__(self,op2): # less than <
        if isinstance(op2,Character):
            return op2._name < self._name
        else:
            raise TypeError
        
    def __gt__(self,op2): # greater than > 
        if isinstance (op2,Character):
            return op2._name > self._name
        else:
            raise TypeError
        
        

#derived avatar class
class Avatar(Character):

    def __init__(self):
        self._GymBadges = 0
        self._starter = " "

    def Avatar_insert(self):
        #exception handling
        try: 
            self._GymBadges = int(input("Please enter the number of gymbadges you've earned so far: "))
            self._starter = input("Please enter the name of your starter: ")

        except ValueError:
            print("Invalid info entered")

    def Avatar_display(self):
        super().display()
        print(self._GymBadges)
        print(self._starter)

    def Avatar_description(self):    
        super().display_history

    
#pokemon class
class Pokemon(Character):        
    def __init__(self):
        self._level = 0
        self._location = " " # This is where the pokemon was caught (route 42)

    def Pokemon_insert(self):
        #exception handling

        try:
            self._level = int(input("Please enter the level of the pokemon: "))
            self._location = input("Please enter where you caught this pokemon: ")

        except ValueError:
            print("Invalid info entered")

    def Pokemon_display(self):
        super().display()
        print(self._level)
        print(self._location)

    def Pokemon_description(self):
        print("Please enter the history of your pokemon or their pokedex entry: ")
        super().description()   
        super().display_history()
 
    def __lt__(self, op2):
        return super().__lt__(op2)
    
    def __gt__(self, op2):
        return super().__gt__(op2)

#champion of the region class
class Champion(Character):
    def __init__(self):
        team_level = np.array(55,56,56,57,58,60)#represents the level of the champions team
        self._ace = " "
        self._region = " " #There is one champion in every region so this asks for the region of that specific champion
    
    def Champion_insert(self):
        #exception handling
        try:
            self._ace = input("Please enter the name of the ace pokemon: ")
            self._region = input("Please enter the name of the region: ")

        except ValueError:
            print("Invalid info entered")

    def Champion_display(self):
        super().display()
        print("The ace pokemon is : " ,self._ace)
        print("The region of the champion is : " ,self._region)

    def Champion_description(self):
        super().display_history


    
