# Classe Pai
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        raise NotImplementedError("Subclasse deve implementar o método falar")

# Classe Filha
class Cachorro(Animal):
    def falar(self):
        return "Au au!"

# Outra Classe Filha
class Gato(Animal):
    def falar(self):
        return "Miau!"

# Uso das classes
cachorro = Cachorro("Rex")
gato = Gato("Whiskers")

print(cachorro.nome)  # Saída: Rex
print(cachorro.falar())  # Saída: Au au!

print(gato.nome)  # Saída: Whiskers
print(gato.falar())  # Saída: Miau!