def calcular_fatorial(numero):
    numero = int(numero)
    if numero < 0:
        return "Fatorial não definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(numero):
            fatorial *= (i + 1)
        return fatorial

n = int(input("Digite um número para calcular o fatorial: "))
resultado = calcular_fatorial(n)
print(resultado)