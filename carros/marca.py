class Marca():
    def __init__(self, id, nome, sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla

    def __str__(self):
        return f"-----MARCA-----\nID: {self.id}\nNome: {self.nome}\nsigla: {self.sigla}"