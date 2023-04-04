nome = "Lucas"
sobrenome = "Ribeiro"
print("Nome: {0}\nSobrenome: {1}".format(nome, sobrenome))

# formatacao
# antes do ponto numeros inteiro depois do ponto decimais
# :08.2f = 8 inteiro sendo que desses 8 2 sao decimais
# :f = float :d = inteiro
print("R$ {:.2f}".format(1.59))
print("R$ {:.3f}".format(1234.5))
print("R$ {:7.2f}".format(1234.5))
print("R$ {:7.2f}".format(4.5)) # ponto no mesmo lugar q o anterior
print("R$ {:07.2f}".format(3.2))
print("R$ {:7d}".format(2))
print("R$ {:2d}".format(45))

# Fstring
print(f"Meu nome é {nome}")
print(f"Meu nome é {nome.upper() + '!' * 3}")