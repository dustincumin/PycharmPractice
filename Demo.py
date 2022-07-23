from contextlib import nullcontext
from pydoc import pipepager
from unicodedata import name
from xmlrpc.server import SimpleXMLRPCDispatcher


class animal:
    name = None
    age =  None
    weight  = None
    color   = None
    owner = None
    def show (self):
        print(f"Name: {self.name}") 
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}")
        print(f"Color: {self.color}")
        print(f"Owner: {self.owner}")
pig = animal()
pig.name = "pig"       
pig.age = "2"
pig.weight = "100"
pig.color = "pink"
pig.owner = "John"

pig.show()
