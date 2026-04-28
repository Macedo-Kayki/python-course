import os
import sqlite3
from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo
from errorlog import log_error

class BancoDeDados:
    def __init__(self, nome_banco="banco.sqlite"):
        self.nome_banco = os.path.join(os.path.dirname(__file__), nome_banco)
        self.conn = None
    
    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
            print("conectado")
        except sqlite3.DatabaseError as e:
            log_error(f"Erro ao conectar ao banco de dados: {e}")
            raise
    
    def criar_tabela_pessoa(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Pessoa(
                                cpf INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                nascimento DATE,
                                oculos BOOLEAN
                                )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"Erro ao criar tabela Pessoa: {e}")
                raise
    
    def criar_tabela_marca(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Marca(
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                sigla TEXT NOT NULL
                                )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"Erro ao criar tabela Marca: {e}")
                raise
    
    def criar_tabela_veiculo(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Veiculo(
                                marca_id INTEGER PRIMARY KEY,
                                placa TEXT NOT NULL,
                                proprietario_cpf TEXT NOT NULL,
                                cor TEXT NOT NULL,
                                FOREIGN KEY(proprietario_cpf) REFERENCES Pessoa(cpf),
                                FOREIGN KEY(marca_id) REFERENCES Marca(id)
                                )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"Erro ao criar tabela Veiculo: {e}")
                raise

    def criar_tabelas(self):
        self.criar_tabela_pessoa()
        self.criar_tabela_marca()
        self.criar_tabela_veiculo()
    
    def criar_pessoa(self, cpf, nome, nasc, oculos):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    f"""INSERT INTO Pessoa VALUES({cpf}, '{nome}', {nasc}, {oculos})"""
                )
                self.conn.commit()
            except sqlite3.DataError as e:
                log_error(f"Dados Incorretos: {e}")
                raise
            except sqlite3.OperationalError as e:
                log_error(f"Erros operacionais: {e}")
                raise
            except sqlite3.IntegrityError as e:
                log_error(f"Violação de restrições: {e}")
                raise

    def criar_marca(self, id, nome, sigla):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    f"INSERT INTO Marca VALUES({id}, '{nome}', '{sigla}')"
                )
                self.conn.commit()
            except sqlite3.DataError as e:
                log_error(f"Dados Incorretos: {e}")
                raise
            except sqlite3.OperationalError as e:
                log_error(f"Erros operacionais: {e}")
                raise
            except sqlite3.IntegrityError as e:
                log_error(f"Violação de restrições: {e}")
                raise

    
    def select(self, select):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    f"""SELECT * FROM {select}"""
                )
                resultado = cursor.fetchall()

                return resultado
            except sqlite3.DatabaseError as e:
                print(f"Erro no banco de dados: {e}")
                raise


if __name__ == "__main__":
    bd = BancoDeDados()
    bd.conectar()
    bd.criar_tabelas()
    bd.criar_marca(1, "Ferrari", "fefa")
    bd.criar_pessoa(152, "Kayki", date(2007, 4, 5), 0)
    pessoinha = bd.select("Marca")
    print(pessoinha)