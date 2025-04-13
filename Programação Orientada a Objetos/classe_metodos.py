class Pessoa:
    contador = 0  # Atributo de classe

    def __init__(self, nome):
        self.nome = nome
        Pessoa.contador += 1

    @classmethod
    def numero_pessoas(cls):
        return cls.contador

pessoa1 = Pessoa("Alice")
pessoa2 = Pessoa("Bob")

print(Pessoa.numero_pessoas())  # 2