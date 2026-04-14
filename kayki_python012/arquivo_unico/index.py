arquivo = open('aula03/manipulando_arquivo/texto.txt')

print('Nome do arquivo: ', arquivo.name)
print('Tamanho do arquivo da posição atual(em bytes): ', arquivo.tell())
print('Modo do arquivo: ', arquivo.mode)
print('Arquivo está fechado? ', arquivo.closed)

arquivo.close()

print('Arquivo está fechado? ', arquivo.closed)