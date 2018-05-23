class Animal:
    def __init__(self, isMammal, isCarnivorous):
        self._isMammal = isMammal
        self._isCarnivorous = isCarnivorous

    def getIsMammal(self):
        return self._isMammal == True

    def getIsCarnivorous(self):
        return self._isCarnivorous == True


class Dog(Animal):
    def __init__(self, greeting):
        Animal.__init__(self, True, True)
        self._greeting = greeting

    def getGreeting(self):
        print("A dog says '{}', is carnivorous, and is a mammal.".format(
            self._greeting))


class Cow(Animal):
    def __init__(self, greeting):
        Animal.__init__(self, True, False)
        self._greeting = greeting

    def getGreeting(self):
        print("A cow says '{}', is not carnivorous, and is a mammal. ".format(
            self._greeting))


class Duck(Animal):
    def __init__(self, greeting):
        Animal.__init__(self, False, False)
        self._greeting = greeting

    def getGreeting(self):
        print("A duck says '{}', is not carnivorous, and is a not a mammal. ".
              format(self._greeting))


dog = Dog("ruff")
cow = Cow("moo")
duck = Duck("quack")

print("Is dog mammal: {}".format(dog.getIsMammal()))
print("Is dog carnivorous: {}".format(dog.getIsCarnivorous()))

print("Is cow mammal: {}".format(cow.getIsMammal()))
print("Is cow carnivorous: {}".format(cow.getIsCarnivorous()))

print("Is duck mammal: {}".format(duck.getIsMammal()))
print("Is duck carnivorous: {}".format(duck.getIsCarnivorous()))

dog.getGreeting()
cow.getGreeting()
duck.getGreeting()