class Pet():
    def __init__(self, name, breed):
        self.name = name
        self.pets = 0

    def add_pets(self, amount, name, breed):
        self.pets += amount
        self.name = name
        self.breed = breed

    def abandon_pets(self, amount, name, breed):
        self.pets -= amount
        self.name = name
        self.breed = breed





    def adopted_pets(self, name, amount, breed):
        self.amount = amount 
        self.name = name
        self.breed = breed

Tabitha = Pet("Tabitha", "Cat")
Tabitha.add_pets(1, "Tabitha", "cat")
# print(f"Your new pet {self.name} the {self.breed} is going to be so happy")


