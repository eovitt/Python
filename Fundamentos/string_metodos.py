texto = "Python String Methods"

# Retorna uma nova string com todas as letras em minúsculas
print(texto.lower())  # Saída: "python string methods"

# Retorna uma nova string com todas as letras em maiúsculas
print(texto.upper())  # Saída: "PYTHON STRING METHODS"

# Converte a primeira letra da string para maiúscula e o restante para minúscula
print(texto.capitalize()) # Saída: "Python string methods"

# Conta quantas vezes a substring aparece na string original.
print(texto.count("t")) # Saída: 3

# Divide a string em uma lista de substrings com base em um caractere delimitador
print(texto.split()) # ['Python', 'String', 'Methods']