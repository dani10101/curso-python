import pendulum
def decorador_ruta(ruta):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Se ha ejecutado la función {func.__name__}")
            resultado = func(*args, **kwargs)
            print(f"En el path {ruta}")
            return resultado
        return wrapper
    return decorador

@decorador_ruta("/escritorio")
def sumar(a, b):
    return a + b

# Al llamar sumar(10, 20), imprimirá el mensaje con su nombre, la ruta y el resultado.
print(sumar(10, 20))
dt = pendulum.now()
def decorador_s(string,string_1):#funcion para decorar
    def decorador(func):#
        def desempaquetar_argumentos(*args,**kwargs):#desempaqueta argumentos de la funcion que usemos para añadir con el decorador
            print("se va a ejecutar esta funcion",func.__name__, "con lo cual puedo imprimir",string + string_1,"en este momento",dt)#aqui se dice el nombre y la hroa de lafuncion añadida
            
            resultado= func(*args,**kwargs)#aqui se alamcena el desmepaquetado de argumentos del afuncion concatenar
            return resultado
        
        return desempaquetar_argumentos
    return decorador

@decorador_s("soy dani","hola")
def concatenar(s,a):
    return s + a
print(concatenar("quetal ","adios"))    