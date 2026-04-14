from esc import escrever
from ler import ler

if __name__ == "__main__":
    caminho_arquivo = 'aula03/manipulando_arquivo/nomes.txt'

    escrever(['kayki', 'macedo', 'raphael'], caminho_arquivo)
    ler(caminho_arquivo)