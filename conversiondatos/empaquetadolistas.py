variable=[1,2,3,4,5,67,]
n1,n2,*resto_numero,_=variable
print(n1,n2,resto_numero)
def suma(*numeros):
    return sum(numeros)
numeros=[2,3,4,5,6,7]
resultado= suma(*numeros)
print(resultado)
def suma1(n1,n2):
    return n1 + n2
diccionario={"n1":10,"n2":45}
resultado=suma1(**diccionario)
print(resultado)
#funcion(*valores_posicon,**posicion_clave:valor)
