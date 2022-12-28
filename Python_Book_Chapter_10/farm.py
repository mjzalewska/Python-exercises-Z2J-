"""
Challenge 10.4
Create a simplified model of a farm:
1. You should have at least four classes: the parent Animal class and at least three child animal classes that
inherit from Animal
2.Each class should have a few attributes and at least one method that models some behaviour appropriate for a
specific animal or all animals - walking, running, eating, sleeping, and so on.
3. Keep it simple. Utilize inheritance. Make sure you output details about the animals and their behaviours.
"""


class Animal:

    def __init__(self, species, name, hunger_lvl=5):
        self.hunger = hunger_lvl
        self.place = ""
        self.species = species
        self.name = name

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def move(self, movement_type, destination):
        self.place = destination
        return f"{self.species} {movement_type}. The new location is{self.place}"

    def make_sound(self, sound):
        return f"{self.species}s {sound}"

    def get_hungry(self, increment):
        self.hunger += increment

    def eat(self, feed, hunger_impact): #get the impact from class Feed
        if hunger_impact > self.hunger:
            self.hunger = 0
        self.hunger -= hunger_impact


class Pig(Animal):
    def make_sound(self, sound="squeal"):
        return f"{self.species}s {sound}"


class Cow(Animal):
    pass


class Chicken(Animal):
    pass


class Feed:
    def __init__(self, name, impact):
        self.name = name
        self.impact = impact

    def reduce_hunger(self):


class CowFeed(Feed):
    pass


class ChickenFeed(Feed):
    pass


class PigFeed(Feed):
    pass
