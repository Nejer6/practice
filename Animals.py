class Animal:
    def __init__(self, name, size, _type):
        self.name = name
        self.size = size
        self.type = _type

    def move(self):
        print(self.name, "moving")


class Cat(Animal):
    def __init__(self, name, size, _type, color):
        super().__init__(name, size, _type)
        self.color = color

    def move(self):
        print(self.name, 'walking')


class Panther(Cat):
    say = '*nothing*'

    def __init__(self, name, size, _type, color, pride):
        super().__init__(name, size, _type, color)
        self.pride = pride

    def attack(self, target):
        print(self.name, 'attack', target.name)


alica = Cat(color='white', name='alica', size='small', _type='predator')
print(alica.color)
alica.move()
jojo = Panther(color='black', name='jojo', size='big', _type='predator', pride='main')
jojo.attack(alica)
