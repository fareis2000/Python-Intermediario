# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

import copy

for item in produtos:
    print(f'{item["nome"]} custa R$ {item["preco"]:.2f}')
print("-" * 20)
print('Produtos com aumento de 10%:')
novos_produtos = copy.deepcopy(produtos)
for item in novos_produtos:
    item['preco'] = item['preco'] * 1.10
formatar = '{nome} custa R$ {preco:.2f}'
for produto in novos_produtos:
   print(formatar.format(**produto))

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)
print('Ordenação por nome:')
for produto in produtos_ordenados_por_nome:
    print(formatar.format(**produto))

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda item: item['preco'])
print('Ordenação por preço:')
for produto in produtos_ordenados_por_preco:
    print(formatar.format(**produto))
