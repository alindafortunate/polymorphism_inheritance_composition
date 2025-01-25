class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound")

    def eat(self):
        print("Animal eats.")


class Dog(Animal):
    def _init__(self, name):
        super().__init__(name)

    def make_sound_dog(self):
        print("Woof")


dog1 = Dog("Simba")
dog1.make_sound_dog()
