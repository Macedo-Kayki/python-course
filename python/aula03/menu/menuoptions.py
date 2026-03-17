import os
from pathlib import Path

def lista(caminho_arquivo):
    listagem = Path(caminho_arquivo)
    for arquivo in listagem.glob('*.txt'):
        print("="*20+"\n"+arquivo.name+"\n"+"="*20)

def leitura(caminho_arquivo, modo):
      with open(caminho_arquivo, modo) as arquivo:
        linhas = arquivo.readlines()
        if (linhas != ""):
            for i, linha in enumerate(linhas, start = 1):
                print(f"{i}ª Linha: {linha}")

def escrita(caminho_arquivo, modo):
    qtd = int(input("Quantas linhas você quer adicionar? "))
    i = 1
    with open(caminho_arquivo, modo) as arquivo:
        while (i <= qtd):
            line = input(f"Digite {i}ª linha: ")
            arquivo.write(line+"\n")
            i = i+1
                    
def edicao(caminho_arquivo, modo):
    with open(caminho_arquivo, modo) as arquivo:
        dados = arquivo.read()
        print(dados)
        qtd = int(input("Quantas linhas você quer adicionar? "))
        i = 1
        while (i <= qtd):
            line = input(f"Digite {i}ª linha: ")
            arquivo.write("\n"+line)
            i = i+1
            
def remocao(caminho_arquivo):
    ctz = input(f"Você tem certeza que deseja deletar o arquivo {caminho_arquivo}? ESSA AÇÃO É IRREVERSÍVEL!!!")
    if ctz.lower == "s" or ctz.lower == "sim":
        os.remove(caminho_arquivo)
    else:
        print("Operação cancelada, retornando ao menu")
        

def caminho():
    diretorio_arquivo = os.path.dirname(os.path.abspath(__file__))
    print(diretorio_arquivo)

def options(modo, caminho_arquivo):
    match modo:
        case "l":
            lista(caminho_arquivo)
        case "r":
            leitura(caminho_arquivo, modo)
        case "w":
            escrita(caminho_arquivo, modo)
        case "r+":
            edicao(caminho_arquivo, modo)
        case "d":
            remocao(caminho_arquivo)
        case "cm":
            caminho()
    input("digite qualquer caractere para continuar: ")