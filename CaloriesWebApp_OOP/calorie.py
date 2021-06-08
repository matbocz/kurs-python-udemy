from temperature import Temperature


class Calorie:
    """
    Represents optimal calorie amount a person needs to take today
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == "__main__":
    temp = Temperature(country="poland", city="slupsk")
    calorie = Calorie(weight=110, height=168, age=24, temperature=temp.get())
    print(calorie.calculate())
