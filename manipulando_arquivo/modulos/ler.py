def ler(caminho_arquivo):
    arquivo = open(caminho_arquivo, 'r')
    linhas = arquivo.readlines()
    for i, linha in enumerate(linhas, start = 1):
        print(f"Linha {i}: {linha}")
    arquivo.close()