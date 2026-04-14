with open("exemplo.txt", "w") as f:
    f.write("exemplo de uso dos métodos do seek() e tell() em Python.")
    f.write("aaaaaaa bbbb cccc dos métodos do seek() e tell() em Python.")
    f.write("dddddd eeeee fffff dos métodos do seek() e tell() em Python.")

with open("exemplo.txt", "r") as f:
    print("Posição inicial do cursor:", f.tell())

    conteudo = f.read(10)
    print("Conteúdo lido: ", conteudo)
    print("Posição do cursor após ler 10 carácteres", f.tell())

    f.seek(0, 1)
    print("Posição do cursor após seek(0, 0): ", f.tell())

    f.seek(15, 0)
    print("Posição do cursor após seek(15, 0):", f.tell())
    parte = f.read(5)
    print("Conteúdo lido após seek(15, 0): ", parte)

    pos_atual = f.tell()
    f.seek(pos_atual - 5, 0)
    print("Posição do cursor após retroceder 5 carácteres", f.tell())
    parte2 = f.read(5)
    print("Conteúdo lido após retroceder 5 carácteres: ", parte2)

    f.seek(0, 2)
    print("Posição do cursor no fim do arquivo: ", f.tell())