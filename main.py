class Cat:
    say = 'Meow'

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def __str__(self):
        return "Cat name:" + self.name

    def __repr__(self):
        return "Cat name:" + self.name

    def say_your_name(self):
        print("Meow, my name is " + self.name + ',', self.say)

    @classmethod
    def print_say(cls):
        print(cls.say)


cats = []
alice = Cat('alice', "red", 2)
jojo = Cat('jojo', "black", 999)
cats.append(alice)
cats.append(jojo)
cats[0].color = "white"
cats[0].say_your_name()
cats[1].say_your_name()
