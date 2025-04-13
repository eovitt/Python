### Tratamento de Exceções ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Exceção base: try except

try:
    print(numberOne + numberTwo)
    print("Não ocorreu um erro")
except:
    # Executa se ocorrer uma exceção
    print("Ocorreu um erro")

# Fluxo completo de uma exceção: try except else finally

try:
    print(numberOne + numberTwo)
    print("Não ocorreu um erro")
except:
    print("Ocorreu um erro")
else:  # Opcional
    # Executa se não ocorrer uma exceção
    print("A execução continua corretamente")
finally:  # Opcional
    # Executa sempre
    print("A execução continua")

# Exceções por tipo

try:
    print(numberOne + numberTwo)
    print("Não ocorreu um erro")
except ValueError:
    print("Ocorreu um ValueError")
except TypeError:
    print("Ocorreu um TypeError")

# Captura das informações da exceção

try:
    print(numberOne + numberTwo)
    print("Não ocorreu um erro")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)