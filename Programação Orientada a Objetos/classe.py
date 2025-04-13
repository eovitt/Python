class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    

pessoa1 = Pessoa("Nex", 24)
pessoa2 = Pessoa("Bob", 30)

print(pessoa1.cumprimentar())
print(pessoa2.cumprimentar())
        