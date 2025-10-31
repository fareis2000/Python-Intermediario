# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):

    def funcao_adicionada(y):
        return funcao(x, y)
    return funcao_adicionada


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

operacao = input('Voce quer somar ou multiplicar? [soma/multiplica]: ')
n = int(input('Digite um número: '))
if operacao == 'soma':
    print(soma_com_cinco(n))
elif operacao == 'multiplica':
    print(multiplica_por_dez(n))
else:
    print('Operação inválida.')
# print(soma_com_cinco(3))
# print(multiplica_por_dez(3))