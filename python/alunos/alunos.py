def criar_registro_notas(arquivo):
    with open(arquivo, "w") as file:
        file.write("Registro de Notas dos Alunos\n")
        file.write("----------------------------\n")

def adicionar_nota(arquivo, aluno, nota):
    try:
        with open(arquivo, "a") as file:
            file.write(f"Aluno: {aluno}\n")
            file.write(f"Nota:{nota}\n")
            file.write("----------------------------\n")
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except IOError:
        print("Ocorreu um erro na abertura do arquivo")
    except ValueError:
        print("Formato inválido encontrado no arquivo")
    except Exception as e:
        print(f"Ocorreu um erro inesperado> {e}")
        raise
    

if __name__ == "__main__":
    arquivo = "alunos/files/notas.txt"

    criar_registro_notas(arquivo)

    adicionar_nota(arquivo, "kayki", 10)
    adicionar_nota(arquivo, "rafael", 10)
    adicionar_nota(arquivo, "carlos", 9.5)
    adicionar_nota(arquivo, "nicolas", 7.5)