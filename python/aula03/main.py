import os

diretorio_arquivo = os.path.dirname(os.path.abspath(__file__))

diretorio_base = "C:\\Users\\AlunoTI\\Desktop\\python"

subdiretorio = "aula03"
nome_arquivo = "dados.txt"

caminho_relativo = os.path.join(diretorio_base, subdiretorio, nome_arquivo)

caminho_absoluto = os.path.abspath(caminho_relativo)

os.remove(caminho_absoluto)

print(f"Caminho relativo: {caminho_relativo}")
print(f"Caminho absoluto: {caminho_absoluto}")
print(f"Diretório Arquivo: {diretorio_arquivo}")
caminho_absoluto = os.path.abspath(caminho_relativo)

