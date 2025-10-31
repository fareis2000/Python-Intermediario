@decorador
def funcion_decorada():
    print("Esta es una función decorada")
    return "Resultado de la función decorada"

resultado = funcion_decorada()
print(resultado)
def decorador(funcion):
    def funcion_interior(*args, **kwargs):
        print("Antes de llamar a la función")
        resultado = funcion(*args, **kwargs)
        print("Después de llamar a la función")
        return resultado
    return funcion_interior

# Uso del decorador

@decorador
def funcion_decorada():
    print("Esta es una función decorada")
    return "Resultado de la función decorada"

resultado = funcion_decorada()
print(resultado)