from ambos import ambos

caminho_arquivo = 'aula03/manipulando_arquivo/carros.txt'

def options():
    opc = int(input("\nEscolha uma das opções abaixo\n1 - Lista de Carros\n2 - Novos Carros\n3 - Editar Carros\n0 - Sair do Sistema\n"))

    chamar_func(opc)

def chamar_func(opc):
    modo = "r", "w"
    if (opc == 1):
        ambos(modo[0], caminho_arquivo)
    elif (opc == 2):
        ambos(modo[1], caminho_arquivo)
        options()

if __name__ == "__main__":
    options()