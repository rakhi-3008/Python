from abc import ABC, abstractmethod     #abstraction base classes

class Animal(ABC) :
    @abstractmethod
    def make_sound(self):   #abstract method
        pass

class Lion(Animal) :
    def make_sound(self):
        print("roar")

class Cow(Animal) :
    def make_sound(self):
        print("moooo")

l1  = Lion()
l1.make_sound()