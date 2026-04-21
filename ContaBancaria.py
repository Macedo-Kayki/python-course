class ContaBancaria:
    def __init__(self, saldo: float, nome: str, conta: int):
        self.__saldo = saldo
        self.nome = nome
        self.conta = conta
    
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def sacar(self, valor):
        if valor > self.__saldo or valor < 0:
            raise ValueError("ERRO: O valor de saque deve ser menor ou igual ao seu saldo e maior que zero.")
        self.__saldo -= valor
        print("="*50+f"\nSaque realizado no valor de: {valor:.2f}\n"+"="*50)

    @saldo.setter
    def depositar(self, valor):
        if valor < 0:
            raise ValueError("ERRO: O valor de deposito deve ser maior que zero.")
        self.__saldo += valor
        print("="*50+f"\nDeposito realizado no valor de: {valor:.2f}\n"+"="*50)

    def __str__(self):
        return "Dados da conta bancária:\n"+"="*50+f"\nNúmero da Conta: {self.conta}\nNome do Titular: {self.nome}\nSaldo da Conta: R$ {self.__saldo:.2f}"

if __name__ == "__main__":
    cb = ContaBancaria(300.5, "Kayki Macedo", 23811570211611)
    cb.sacar = (100)
    cb.depositar = (1000)
    print(cb)