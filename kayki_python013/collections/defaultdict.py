from collections import defaultdict

estudantes_por_sala = defaultdict(list)

estudantes_por_sala['B'].append('Raphael')
estudantes_por_sala['A'].append('Gilson')
estudantes_por_sala['A'].append('Sara')

print(dict(estudantes_por_sala))