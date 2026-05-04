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
    
    def atualizar_veiculo(self, veiculo):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("UPDATE Veiculo SET marca_id = ?, placa = ?, cor = ? WHERE proprietario_cpf = ?"
                               (veiculo.marca_id, veiculo.placa, veiculo.cor, veiculo.proprietario_cpf))
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"Erro ao dar update no veiculo com o proprietario: {veiculo.proprietario_cpf}")
                raise

    def apagar_veiculo(self, veiculo):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM Veiculo WHERE placa = ?",
                               (veiculo.placa,))
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"Erro ao apagar veiculo: {e}")
                raise

    def buscar_pessoas(self):
        pessoas = []
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "SELECT * FROM Pessoa"
                )
                for row in cursor.fetchall():
                    cpf, nome, nascimento, oculos = row
                    pessoas.append(Pessoa(cpf, nome, nascimento, oculos))
            except sqlite3.DatabaseError as e:
                log_error(f"Erro no banco de dados: {e}")
                raise
        return pessoas
    
    def buscar_pessoa_cpf(self, cpf):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Pessoa WHERE cpf = ?", (cpf,))
                row = cursor.fetchone()
                if row:
                    cpf, nome, nascimento, oculos = row
                    return Pessoa(cpf, nome, nascimento, oculos)
            except sqlite3.DataError as e:
                log_error(f"Dados Incorretos: {e}")
                raise
        return None
    
    def buscar_marca_id(self, marca):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Marca WHERE id = ?", (marca,))
                row = cursor.fetchone()
                if row:
                    id, nome, sigla = row
                    return Pessoa(id, nome, sigla)
            except sqlite3.DataError as e:
                log_error(f"Dados Incorretos: {e}")
                raise
        return None

    
    def buscar_veiculos(self):
        veiculos = []
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "SELECT * FROM Veiculo"
                )
                for row in cursor.fetchall():
                    placa, cor, proprietario_cpf, marca_id = row
                    proprietario = self.buscar_pessoa_cpf(proprietario_cpf)
                    marca = self.buscar_marca_id(marca_id)
                    veiculos.append(Veiculo(placa, cor, proprietario, marca))
            except sqlite3.DatabaseError as e:
                log_error(f"Erro no banco de dados: {e}")
                raise
        return veiculos

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None

if __name__ == "__main__":
    bd = BancoDeDados()
    bd.conectar()
    bd.criar_tabelas()
    bd.criar_marca(1, "Ferrari", "fefa")
    bd.criar_pessoa(152, "Kayki", date(2007, 4, 5), 0)
    busca = bd.buscar_pessoas()
    print(busca)
