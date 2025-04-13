# Exemplo com operador 'is'
x = [1, 2, 3]
y = x  # y aponta para o mesmo objeto que x

print(x is y)  # True

# Exemplo com operador 'is not'
z = [1, 2, 3]
print(x is not z)  # True (x e z não são o mesmo objeto)