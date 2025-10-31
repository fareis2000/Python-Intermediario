# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')

pessoas = ['Luiz', 'Andre', 'Maria', 'Helena']
camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G'],
    ['Masculina', 'Feminina'],
    ['Algodão', 'Poliéster'],
    ['Curta', 'Longa'],
    ['Estampada', 'Lisa']
]

print('Combinação - Ordem não importa')
print_iter(combinations(pessoas, 2))

print('Permutação - Ordem importa')
print_iter(permutations(pessoas, 2))

print('Produto - Ordem importa e repete valores únicos')
print_iter(product(*camisetas))