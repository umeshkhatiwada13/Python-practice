class Footballer:
    def __init__(self, name, age, country, position, is_starter):
        self.name = name
        self.age = age
        self.country = country
        self.position = position
        self.is_starter = is_starter

    # Object function
    def is_spanish(self):
        if self.country.lower() == 'spain':
            return True
        else:
            return False
