class Retangulo:
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    @property
    def area(self):
        return self.__largura * self.__altura

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self.__largura = valor
        else:
            print("Largura deve ser positiva.")

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self.__altura = valor
        else:
            print("Altura deve ser positiva.")

retangulo = Retangulo(5, 10)
print(retangulo.area)  # 50

retangulo.largura = 8
print(retangulo.area)  # 80