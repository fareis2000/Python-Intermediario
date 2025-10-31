#groupby - agrupa elementos consecutivos de un iterable que son iguales
from itertools import groupby

alunos = [ 
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Andre', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Helena', 'nota': 'B'},
    {'nome': 'Fabio', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'B'},
]

def ordena(item):
    return item['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(f'Grupo {chave}:')
    for aluno in grupo:
        print(aluno)
    print() 












# alunos_agrupados = sorted(alunos, key=lambda aluno: aluno['nota'])

# for aluno in alunos_agrupados:
#     print(aluno)


# alunos = ['a', 'b', 'c']
# grupos = groupby(alunos)
# print(list(grupos))

# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))