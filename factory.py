class Dog:
    """ Dog class """
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "woof!"


class Cat:
    """ Dog class """
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "miao!"


def get_pet(pet = "dog"):
    """ the factory method """

    pets = dict(dog = Dog("Bo"), cat = Cat("Jianbo"))

    return pets[pet]

d = get_pet("dog")
c = get_pet("cat")

print(c.speak())
