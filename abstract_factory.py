class Dog:
    """ One of objects to be returned """
    def speak(self):
        return "woof!"

    def __str__(self):
        return "Dog"

class DogFactory:
    """ concrete Factory """
    def get_pet(self):
        """ return a Dog object """
        return Dog()

    def get_food(self):
        """ Return a Dog food object """
        return "Dog food"

class PetStore:
    """ petStore as our abstract Factory """
    def __init__(self,pet_factory = None):
        self._pet_factory = pet_factory


    def show_pet(self):

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("our pet is '{}' !".format(pet))
        print("our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))

# create a concrete Factory
factory = DogFactory()

# create a pet store housing our abstract factory
shop = PetStore(factory)

# invoke the utility method to how the detail of our pet
shop.show_pet()
