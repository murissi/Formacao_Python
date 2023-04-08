class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibeNome_sobrenome(self):
        print(f"Nome: {self.nome}\nSobrenome: {self.sobrenome}")


pessoa = Pessoa("Chalita", "Steppat")
# VARIAVEL QUE NAO REFENCIA NENHUM OBJETO
outraRef = None
pessoa.exibeNome_sobrenome()

