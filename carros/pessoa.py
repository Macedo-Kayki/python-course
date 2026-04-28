class Pessoa():
    def __init__(self, cpf, nome, nascimento, oculos):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.oculos = oculos

    def __str__(self):
        self.oculos = "Sim" if self.oculos else "Não"
        return f"-----PESSOA-----\cpf: {self.cpf}\nNome: {self.nome}\nData de nascimneto: {self.nascimento}\nOculos: {self.oculos}"