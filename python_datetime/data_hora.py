from datetime import date

data_atual = date.today()
print(data_atual)

data_em_texto = f"{data_atual.day}/{data_atual.month}/{data_atual.year}"
print(data_em_texto)

# strtime()
data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)