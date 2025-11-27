class Animal:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_animal(name):
        return isinstance(name, str)
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        return "Meow!"