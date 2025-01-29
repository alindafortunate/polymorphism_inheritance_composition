class MathUtils:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def about_calculator(self):
        print(f"{self.name},{self.model}")

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b


calculator1 = MathUtils("Smart Calculator", "XY001")
calculator1.about_calculator()

print(MathUtils.add(2, 3))
print(MathUtils.multiply(2, 3))
