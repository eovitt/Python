lista = ['Python', 'Academy', 2021]
print(lista)

frutas = ['Maça', 'Banana', 'Jaca', 'Melão', 'Abacaxi']
print(frutas[0])  # Saída: "Maça"


# Classifica a lista em ordem crescente.

lista_numerica = [3,6,9,1,2,4,7,5,8,10]
lista_numerica.sort()
print(lista_numerica)  

# Adiciona um único elemento à lista.

lista_numerica.append(11)
print(lista_numerica)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Adiciona vários elementos à lista

lista_numerica.extend([12,13,14,15,16,17,18,19])
print(lista_numerica) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Retorna a primeira ocorrência de um valor especificado.

print(lista_numerica.index(4)) # 3

# Retorna o item com o valor máximo na lista.

print(max(lista_numerica)) # 19