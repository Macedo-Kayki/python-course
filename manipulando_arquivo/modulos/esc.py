def escrever(nomes: list, caminho_arquivo):
    arquivo = open(caminho_arquivo, 'w')

    for nome in nomes:
        arquivo.writelines(nome+"\n")
    arquivo.close()