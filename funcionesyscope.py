
#hacer una funcion que desmpaqueteun diccionario
def concatenar(**contexto):
    string_final = ""
    print(f"Has introducido este contexto {contexto}")
    for string in contexto.values():
        string_final += string
    return string_final

string_compuesto = concatenar(a="Esto", b=" es", c=" un", d=" string!")
print(string_compuesto)
def sumarnumerosdicionario(**numeros):#numeros es una variable que usare mas tarde para guardar el dicionario
    print("este es el namespace local" ,locals())
    acumulador= 0#acumulo el resultado de la suma de los valores del diccionario
    for numero in numeros.values():#itero sobre los valores del dccionario
        acumulador += numero
    return f"{acumulador}"
print(sumarnumerosdicionario(uno=1,dos=2,tres=3))#guardo en esta variable la funcion y sus argumentos en bruto 
#variable = funcion(clave=valor,clave1=valor=1)
#este scope es global por lo tanto el namespace es global
#sintaxis funciones con desempaquetado por dicionario
print(globals())
conversion= lambda decimal: hex(decimal)
print(conversion(10))
def funcion_principal(*n):
    return n[0]*n[1]
def funcion_anidada(func,n):
    return func(n)

resultado=funcion_principal(1,2)
print(funcion_principal(1,2))
