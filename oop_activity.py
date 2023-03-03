class ZooAnimal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

class Zoo:
    def __init__(self):
        self.animals_in_zoo = []
        
    def add_animal(self, animal):
        self.animals_in_zoo.append(animal)
        print(f"{animal.name} has been added.")


    def remove_animal(self, name):
        for animal in self.animals_in_zoo():
            if name in animal:
                return name
    
    def get_animals_by_species(self, species):
        list_by_species = []
        for animal in self.animals_in_zoo:
            if species in animal:
                list_by_species.append(animal.name)
        return list_by_species
    
    def average_age(self):
        sum = 0
        for age in self.animals_in_zoo:
            sum += age.age
        avg = round(sum / len(self.animals_in_zoo), 1)
        return avg




lion = ZooAnimal("Simba", "Lion", 5)
giraffe = ZooAnimal("Melman", "Giraffe", 7)
elephant = ZooAnimal("Dumbo", "Elephant", 10)
zoo = Zoo()
zoo.add_animal(lion)
zoo.add_animal(giraffe)
zoo.add_animal(elephant)
print(zoo.average_age())
print(zoo.remove_animal("Simba"))
# print(zoo.get_animals_by_species("Giraffe"))
