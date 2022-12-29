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

    def __init__(self, species, name, age, hunger_lvl=5, location=0):
        self.species = species
        self.name = name
        self.age = age
        self.hunger = hunger_lvl
        self.location = location

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def move(self, movement_type, distance):
        self.location += distance
        return f"{self.name} {movement_type}, moved by {distance} meters"

    def make_sound(self, sound):
        return f"{self.name} just {sound}ed"

    def get_hungry(self, increment):
        if self.location != 0:
            self.hunger += increment
        if self.hunger > 20:
            return f"{self.name} just got really hungry! Hunger level is {self.hunger}. Time to eat!"
        else:
            return f"{self.name} got a little hungry. Hunger level is {self.hunger}. Let's wait a bit"

    def eat(self, feed):
        if self.hunger < feed.impact:
            self.hunger = 0
        self.hunger -= feed.impact
        return f"{self.name} just ate a nutritious meal. Hunger decreased to {self.hunger} "


class Pig(Animal):
    def make_sound(self, sound="squeal"):
        return f"{self.name} just {sound}ed"


class Cow(Animal):
    def make_sound(self, sound="moo"):
        return f"{self.name} just {sound}ed"


class Chicken(Animal):
    def make_sound(self, sound="cluck"):
        return f"{self.name} just {sound}ed"

    def lay_eggs(self):
        if self.age > 0.5 and self.hunger < 20:
            return "Let's lay some eggs"


class Feed:
    def __init__(self, name, impact, animal):
        self.name = name
        self.impact = impact
        self.animal = animal


corn = Feed('corn', 10, {1: 'chicken', 2: 'pig'})
potatoes = Feed('potatoes', 15, {1: 'pig'})
grass = Feed('grass', 5, {1: 'cow'})
straw = Feed('grass', 5, {1: 'cow'})

Bobby = Pig('pig', 'Bobby', '2', 10, 0)
print(Bobby)
print(Bobby.move('walks slowly', 0.2))
print(Bobby.make_sound())
print(Bobby.get_hungry(20))
print(Bobby.eat(corn))

Clara = Cow('cow', 'Clara', 10, 0)
print(Clara)
print(Clara.move('moves leisurely', 0.05))
print(Clara.make_sound())
print(Clara.get_hungry(5))
print(Clara.eat(grass))

Mandy = Chicken('chicken', 'Mandy', 1.5, 10)
print(Mandy)
print(Mandy.move('runs', 15))
print(Mandy.make_sound())
print(Mandy.get_hungry(30))
print(Mandy.eat(corn))
