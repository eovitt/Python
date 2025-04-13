from abc import ABC, abstractmethod

class Comando(ABC):

    @abstractmethod
    def executar(self):
        pass

class ComandoLigarLuz(Comando):
    def __init__(self, luz):
        self._luz = luz

    def executar(self):
        self._luz.ligar()

class ComandoDesligarLuz(Comando):
    def __init__(self, luz):
        self._luz = luz

    def executar(self):
        self._luz.desligar()

class Luz:
    def ligar(self):
        print("Luz ligada")

    def desligar(self):
        print("Luz desligada")

class ControleRemoto:
    def __init__(self):
        self._comando = None

    def definir_comando(self, comando):
        self._comando = comando

    def pressionar_botao(self):
        self._comando.executar()

# Teste
luz = Luz()
comando_ligar = ComandoLigarLuz(luz)
comando_desligar = ComandoDesligarLuz(luz)

controle = ControleRemoto()
controle.definir_comando(comando_ligar)
controle.pressionar_botao()  # Luz ligada

controle.definir_comando(comando_desligar)
controle.pressionar_botao()  # Luz desligada