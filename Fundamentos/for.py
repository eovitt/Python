#  for é usado para iterar sobre uma sequência de dados (como uma lista, tupla ou string) e executar um conjunto de instruções para cada item. 

# Usando for para iterar sobre um intervalo de 1 a 5

for i in range(1,6):
    print(i)

# Dicionário com alguns pares chave-valor

idades = {"Ana": 30, "João": 25, "Maria": 28}

# Usando for para iterar sobre as chaves e valores do dicionário

for nome, idade in idades.items():
    print(f"{nome} tem {idade} anos")