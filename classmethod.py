# Application of class method.


class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def introduction(self):
        print(f"I am {self.name} and {self.age} years.")

    @classmethod
    def count_instances_created(cls):
        print(f"{cls.count}")


alinda = Person("Alinda", 23)
fortunate = Person("Fortunate", 25)
person3 = Person("Tesfu", 26)
person4 = Person("Mariam", 25)
Person.count_instances_created()
