import pickle

dados = {"nome": "Raphael", "idade": 41, "profissão": "Desenvolvedor"}

def create_pickles(name, mode):
    try:
        with open (name, mode) as save_binary:
            pickle.dump(dados, save_binary)
        print("Dados salvos com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")

def load_pickles(name, mode):
    try:
        with open (name, mode) as carrega_binario:
            dados_carregados = pickle.load(carrega_binario)
        print("Dados carregados com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")