from datetime import datetime, timezone, timedelta

data_horas_atuais = datetime.now()
data_horas_atuais =  data_horas_atuais.strftime('%d/%m/%Y %H:%M')

print(data_horas_atuais)

# Convertendo string em datetime

data_hora_texto = '01/03/2018 12:30'
data_hora_texto = datetime.strptime(
    data_hora_texto,
    '%d/%m/%Y %H:%M')

print(data_hora_texto)

data_horas = datetime.now()
diferenca = timedelta(hours=-3)
fuso_horario = timezone(diferenca)
print(fuso_horario)

data_e_hora_sao_paulo = data_horas.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)