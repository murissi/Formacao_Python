class Funcionario:

    def __init__(self, nome):
        self.nome = nome

    def registro_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa..')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def buscar_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Junior(Alura):
    pass


# Heranca Multipla
class Pleno(Caelum, Alura):
    pass

jose = Junior('jose')
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()

luan =  Pleno('luan')
luan.busca_perguntas_sem_resposta()
luan.buscar_cursos_do_mes()
luan.mostrar_tarefas()

#MRO
# busca por metodos hierarquia
# 1. pleno
# 2. alura > funcionario
# 3. caeluma
# 4. Caelum

# Mixins
class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Senior(Alura, Caelum, Hipster):
    pass

lucas = Senior('Lucas')
print(lucas)
