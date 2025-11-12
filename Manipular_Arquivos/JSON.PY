import json
caminho_arquivo = 'C:\\Users\\farei\\OneDrive\\Documentos\\Fabio\\Fabio\\Estudos_Python\\Intermediario\\Manipular_Arquivos\\'
caminho_arquivo += 'aula117.json'

pessoa = {
    'nome': 'Fabio',
    'idade': 30,
    'endereco': {
        'rua': 'Rua ABC',
        'numero': 123,
        'cidade': 'São Paulo'
    },
    'telefones': ['1234-5678', '9876-5432'],
    'altura': 1.90,
    'dev': True,
    'nada': None,
    'numeros preferidos': (7, 13, 42)
}

# with open(caminho_arquivo, 'w', encoding='utf8') as arquivo_json:
#     json.dump(pessoa, arquivo_json, indent=2, ensure_ascii=False)

with open(caminho_arquivo, 'r', encoding='utf8') as arquivo_json:
    pessoa_carregada = json.load(arquivo_json)
    print(pessoa_carregada)