from datetime import date


class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def dias_vividos(self):
        return (date.today() - self.data_nascimento).days

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        if not isinstance(value, date):
            raise ValueError("data_nascimento deve ser um obj do tipo date")
        self._data_nascimento = value


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

p1 = Pessoa('Lucas', date(2000, 8, 19))
print(p1.dias_vividos())
print(p1.data_nascimento)