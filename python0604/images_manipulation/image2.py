import os

def save_binary(dados_binarios_nome, dados_binarios):
    try:
        with open(dados_binarios_nome, "wb") as salva_binario:
            salva_binario.write(dados_binarios)
        print("Dados binários salvos com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados binários: {e}")


def load_binary(dados_binarios_nome):
    if os.path.exists(dados_binarios_nome):
        try:
            with open(dados_binarios_nome, "rb") as carrega_binario:
                dados_carregados = carrega_binario.read()
            print("Dados binários carregados com sucesso:", dados_carregados)
        except Exception as e:
            print(f"Ocorreu um erro ao carregar os dados binários: {e}")
    else:
        print(f"O arquivo binário '{dados_binarios_nome}' não foi encontrado na pasta")

if __name__ == "__main__":
    diretorio_atual =  os.path.dirname(os.path.abspath(__file__))
    dados_binarios_nome = os.path.join(diretorio_atual, "img/dados_puros.bin")
    dados_binarios = b"\x00\x01\x02\x03\x04\x05"
    save_binary(dados_binarios_nome, dados_binarios)
    load_binary(dados_binarios_nome)