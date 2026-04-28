from pessoa import Pessoa
from marca import Marca

class Veiculo():
    def __init__(self, placa, cor, proprietario_cpf: Pessoa, marca_id: Marca):
        self.placa = placa
        self.cor = cor
        self.proprietario_cpf = proprietario_cpf
        self.marca_id = marca_id
    
    def __str__(self):
        return f"-----VEICULO-----\nplaca: {self.placa}\ncor: {self.cor}\nproprietario_cpf: {self.proprietario_cpf}\nMarca ID: {self.marca_id}"