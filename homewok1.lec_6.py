# all the classes of different animals in our possession.
class Geese:
    def __init__(self, name, feed, egg_production,weight, sound):
        self.name = name
        self.feed = feed
        self.egg_production = egg_production
        self.weight = weight
        self.sound = sound

class Chicken:
    def __init__(self, name, feed, egg_production, weight, sound):
        self.name = name
        self.feed = feed
        self.egg_production = egg_production
        self.weight = weight
        self.sound = sound

class Duck:
    def __init__(self, name, feed, egg_production, weight,  sound):
        self.name = name
        self.feed = feed
        self.egg_production = egg_production
        self.weight = weight
        self.sound = sound

class Cow:
    def __init__(self, name, feed, milk_production, weight, sound):
        self.name = name
        self.feed = feed
        self.milk_production = milk_production
        self.weight = weight
        self.sound = sound

class Goat:
    def __init__(self, name, feed, milk_production, weight, sound):
        self.name = name
        self.feed = feed
        self.milk_production = milk_production
        self.weight = weight
        self.sound = sound


class Sheep:
    def __init__(self, name, feed, wool_production, weight, sound):
        self.name = name
        self.feed = feed
        self.wool_production = wool_production
        self.weight = weight
        self.sound = sound

# what they need
def eat(self, food):
    if self.feed < 100:
        self.feed += food
    else:
        print('Not hungry anymore')

#what they can give (produce)

def milking(self, production):
    if self.milk_production > 0:
        self.milk_production += production * 2
        self.feed -= production * 2
    else:
        print('Milking is done for today!')

def Wool(self, production):
    if self.wool_production > 0:
        self.wool_production += production * 2
        self.feed -= production * 2
    else:
        print('This animal can not give any more wool')

def eggs(self, production):
    if self.egg_production > 0:
        self.egg_production += production * 2
        self.feed -= production * 2
    else:
        print('There is no more eggs to collect here')

# Animals names and stuff

#geeses

Grey = Geese('Grey', 100, 5, 3, 'honking')

White = Geese('White', 100, 3, 3.2, 'honking')

#chickens

Koko = Chicken('Koko', 100, 7, 3.4, 'Cococo')

Crowie = Chicken('Crowie', 100, 9, 3.6, 'Cococo')

#ducks

Krakva = Duck('Krakva', 100, 7, 1.2, 'quacking')

#cows

Manka = Cow('Manka', 100, 20, 100, 'mooo')

#goats

Roga = Goat('Roga', 100, 20, 50, 'bleat')

Kopyta = Goat('Kopyta', 100, 20, 56, 'bleat')


#sheeps

Barashek = Sheep('Barashek', 100, 10, 45, 'baa')


Kydrav = Sheep('Kydrav', 100, 10, 70, 'baa')

# calculate weight of all the animals

#def weight_all():

all_animals_dict = {Grey.name: Grey.weight, White.name: White.weight, Koko.name: Koko.weight, Crowie.name: Crowie.weight, Krakva.name: Krakva.weight, Manka.name: Manka.weight, Roga.name: Roga.weight, Kopyta.name: Kopyta.weight, Barashek.name: Barashek.weight, Kydrav.name: Kydrav.weight}

print(sum(all_animals_dict.values()))

# find the animal that weight heviest and print its name

heaviest_animal_is_name = max(all_animals_dict, key=all_animals_dict.get)
print("The farm animal is:", heaviest_animal_is_name)




