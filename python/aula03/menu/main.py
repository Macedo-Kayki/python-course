import os
from menuoptions import options

diretorio_arquivo = os.path.dirname(os.path.abspath(__file__))

diretorio_base = "C:\\Users\\AlunoTI\\Desktop\\python\\aula03"

subdiretorio = "menu"

def menu():
    opc = int(input("\nEscolha uma das opções abaixo:\n"
            +"="*20+"\n1 - Listar arquivos\n"+"="*20+
          "\n2 - Visualizar arquivo\n"+"="*20+"\n3 - Criar arquivo\n"
          +"="*20+"\n4 - Editar arquivo\n"+"="*20+"\n5 - Deletar arquivo\n"
          +"="*20+"\n6 - Obter caminho do arquivo\n"
          +"="*20+"\n0 - Fechar menu\n"+"="*20+"\n"))

    match opc:
        case 1:
            nome_arquivo = ""
        case 2:
            nome_arquivo = input("Digite o nome do arquivo que você está procurando: ")
        case 3:
            nome_arquivo = input("Digite o nome do novo arquivo: ")
        case 4:
            nome_arquivo = input("Digite o nome do arquivo que você deseja editar: ")
        case 5:
            nome_arquivo = input("Digite o nome do arquivo que você deseja deletar (AÇÃO IRREVERSÍVEL): ")
        case 6:
            nome_arquivo = input("Digite o nome do arquivo que você deseja obter o caminho: ")
        case 0:
            exit

    if nome_arquivo != "":
        caminho_arquivo = os.path.join(diretorio_base, subdiretorio, nome_arquivo+".txt")
    else:
        caminho_arquivo = os.path.join(diretorio_base, subdiretorio)
        
    return openoption(opc, caminho_arquivo)

def openoption(opc, caminho_arquivo):
    modo = "r", "w", "d", "l", "cm", "r+"
    match opc:
        case 1:
            options(modo[3], caminho_arquivo)
        case 2:
            options(modo[0], caminho_arquivo)
        case 3:
            options(modo[1], caminho_arquivo)
        case 4:
            options(modo[5], caminho_arquivo)
        case 5:
            options(modo[2], caminho_arquivo)
        case 6:
            options(modo[4], caminho_arquivo)
        
if __name__ == "__main__":
    while True:
        menu()