# Dependency Inversion Principal
# High level module should not directly depend on
# low level modules, instead they should depend on
# abstraction

from enum import Enum
from abc import abstractmethod
from typing import Type


class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children(self, name):
        pass


# low level module
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations: list[tuple[Person, int, Person]] = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child),
        )
        self.relations.append(
            (child, Relationship.CHILD, parent),
        )

    def find_all_children(self, name):
        for r in self.relations:
            if r[0].name.lower() == name.lower() and r[1] == Relationship.PARENT:
                yield r[2]


# high level module
class Research:
    def __init__(self, name: str, browser: Type[RelationshipBrowser]) -> None:
        for p in browser.find_all_children(name):
            print(f"{name} has a child named {p.name}")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Mary")
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)
research = Research("john", relationships)
