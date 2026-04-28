from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

if __name__ == "__main__":
    veiculo = Veiculo()
    pessoa = Pessoa()
    marca = Marca()

    pessoa(152, "Kayki", date(2007, 4, 5), 0)
    marca(1, "Ferrari", "Fefa")
    veiculo(171, "preto", 152, 1)
