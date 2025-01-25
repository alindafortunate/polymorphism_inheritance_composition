class Flyer:
    def fly(self):
        print("Flying...")


class Swimmer:
    def swim(self):
        print("Swimming...")


class Duck(Flyer, Swimmer):
    def swim(self):
        print("I am a duck and I can swim.")


duck = Duck()
swimmer = Swimmer()
duck.swim()
swimmer.swim()




