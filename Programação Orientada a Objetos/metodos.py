class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

livro = Livro("1984", "George Orwell")
print(livro)  # 1984 por George Orwell