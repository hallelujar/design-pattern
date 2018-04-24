class Borg:
    """Borg class making class attributes global"""
    _shared_state = {} # attributes dictionary

    def __init__(self):
        self.__dict__ = self._shared_state # make it on attributes dictionary

class Singleton(Borg): # inherits from the Borg class
    """ this class now shares all its attributes among its various instances"""
    # this essentially makes the Singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # update the attribute dictionary by inserting a new key-balue pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # returns the attribute dictionary for printing
        return str(self._shared_state)

# let's create a singleton object and add our first acronym
x = Singleton(HTTP = "Hyper Text Tranfer Protocol")
# print the object
print(x)


# lets create another singleton object and if it refers to the same attribute dictionary by adding another acronym
y = Singleton(SNMP = "Simple Network Management Protocol")
# print the object
print(y)

z = Singleton(ABC = "ABC")
print(z)

print(x)
