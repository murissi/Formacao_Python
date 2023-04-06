# Manipulando arquivos

arquivo = open("contatos.txt", "a")

arquivo.write("Hello, World!")

arquivo.close()

arquivo = open("contatos.txt", "r")
print(arquivo.readlines())

arquivo.close()
