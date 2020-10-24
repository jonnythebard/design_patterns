"""
High-level modules should not depend on low-level modules.
Both should depend on abstractions (e.g. interfaces).

Abstractions should not depend on details.
Details (concrete implementations) should depend on abstractions.
"""
import abc
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abc.abstractmethod
    def find_all_children(self, name):
        pass


class Relationships(RelationshipBrowser):
    """low level module"""
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    """high level module"""
    # def __init__(self, relationships):
    #     relations = relationships.relations     # if low level module changes, everything will be ruined.
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children('John'):
            print(f'John has a child called {p}.')


if __name__ == '__main__':
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)
