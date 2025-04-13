class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, quantia):
        if quantia > 0:
            self.__saldo += quantia

    def sacar(self, quantia):
        if 0 < quantia <= self.__saldo:
            self.__saldo -= quantia

    def mostrar_saldo(self):
        return self.__saldo

# Criando uma instância da ContaBancaria
conta = ContaBancaria("Bob", 1000)

# Depositando dinheiro
conta.depositar(500)

# Sacando dinheiro
conta.sacar(200)

# Mostrando o saldo atual
print("Saldo:", conta.mostrar_saldo())