class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animals):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animals):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Meow!"

class Owner:
    def __init__(self, owner_name):
        self.owner_name = owner_name

    def owns(self, pet: Animals):
        print(f"{self.owner_name} owns a pet named {pet.name}.")
