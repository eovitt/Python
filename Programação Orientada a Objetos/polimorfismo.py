class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Gato(Animal):
    def falar(self):
        return "Miau"

def fazer_animal_falar(animal):
    print(animal.falar())

cachorro = Cachorro()
gato = Gato()

fazer_animal_falar(cachorro)
fazer_animal_falar(gato)