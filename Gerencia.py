from abc import ABC, abstractmethod

class GerenciadorFinanceiro(ABC):
    @staticmethod
    def executar_pagamento(p):
        print(f"\nIniciando transação em {Pagamento}")

class Pagamento(GerenciadorFinanceiro):
    def __init__(self, valor: float, status: str):
        self.valor = valor
        self.status = status
        self.status = "Pendente"
    
    @abstractmethod
    def processar(self):
        pass
    
    @abstractmethod
    def gerar_recibo(self):
        pass

    def _validar_valor(self):
        return self.valor > 0


class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao, valor, bandeira):
        super().__init__(valor)
        self.numero_cartao = numero_cartao
        self.valor = valor
        self.bandeira = bandeira

    def processar(self):
        if self._validar_valor() and len(self.numero_cartao) == 16:
            self.status = "Aprovado"
            print(f"Comunicando com a operadora {self.bandeira}...Sucesso")

    def gerar_recibo(self):
        return f"RECIBO DO CARTÃO: R$ {self.valor} | FINAL: "


class PagamentoPix(Pagamento):
    def __init__(self, valor, )
    
    def processar(self):
        if self._validar_valor() and len(self.numero_cartao) == 16:
            self.status = "Concluído"
            print(f"Comunicando com a operadora {self.bandeira}...Sucesso")
    
    def gerar_recibo(self):
        return f"RECIBO PIX: R$ {self.valor} | CHAVE: "
    
    def gerar_qr_code(self):
        return "000020123572BR.GOV.BCB.PIX0111..."