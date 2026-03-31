from collections import namedtuple

Ponto = namedtuple('Ponto', ['x', 'y'])

meu_ponto = Ponto(10, 20)

print(meu_ponto.x)
print(meu_ponto[1])