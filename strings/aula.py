url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

# Fatiamento
texto = "abcde"

# Imutabilidade de Strings no Python
palavra = "abc"
palavra = "def"

'''
    Quando referenciamos uma nova String a antiga string "abc
    deixa de ser referenciada, e o garbage collector exclui ela
'''

# Alterando a string
palavra = "abc"
print(palavra[0])
palavra[0] = "x"