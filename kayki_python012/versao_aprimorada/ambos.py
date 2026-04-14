def leitura(caminho_arquivo, modo):
    with open(caminho_arquivo, modo) as arquivo:
        linhas = arquivo.readlines()
        if (linhas != ""):
            for i, linha in enumerate(linhas, start = 1):
                print(f"Linha {i}: {linha}")

def escrita(caminho_arquivo, modo):
        qtd = int(input("Quantos carros você quer adicionar? "))
        i = 1
        with open(caminho_arquivo, modo) as arquivo:
            while (i <= qtd):
                carro = input(f"Digite o carro da linha {i}: ")
                arquivo.write(carro+"\n")
                i = i+1

def editar(caminho_arquivo):
    pass
    
def ambos(modo, caminho_arquivo):
    if (modo == "r"):
        leitura(caminho_arquivo, modo)
    elif (modo == "w"):
        escrita(caminho_arquivo, modo)