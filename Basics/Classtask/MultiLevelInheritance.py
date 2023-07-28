
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Mammal(Animal):
    def __init__(self, name, mammal_type):
        super().__init__(name)
        self.mammal_type = mammal_type

    def make_sound(self):
        print(f"{self.name} makes a normal sound.")



class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name, mammal_type="Dog")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} barks.")


# Create instances of the classes and demonstrate multilevel inheritance
if __name__ == "__main__":
    animal1 = Animal("Generic Animal")
    animal1.make_sound()

    mammal1 = Mammal("Mammal1", "Generic Mammal")
    mammal1.make_sound()

    dog1 = Dog("Buddy", "Golden Retriever")
    dog1.make_sound()
