import copy

"""
To implement prototype, partially construct an object and store it somewhere
The stored object is a prototype object.
Deep copy the prototype.
Customize the resulting instance.
A factory provides a convention API for using prototypes.
"""


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


if __name__ == "__main__":
    john = Person("John", Address("123 London Road", "London", "UK"))
    print(john)

    # john is a prototype of jane.
    jane = copy.deepcopy(john)
    jane.name = "Jane"
    jane.address.street_address = "124 London Road"
    print(john, jane)
