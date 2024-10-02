#introducir un numero hasta que se introduzca 0 y sumar los numeros entre si
def funcion_suma():
    numeros=input("añade una lista de numeros separados por ,")
    lista_string=[]
    lista_string=numeros.split(",")
    lista_int=[int(t) for t in lista_string] #compresion de listas para cambiar los tipos de datos a enteros
         
    print(sum(lista_int))#suma los elementos de la lista entre si
        
            
funcion_suma()  
def suma_hasta_cero():
    
    suma=[]
    
    numero=1
     
    while numero !=0:
        numero = int(input("introduce un numero,0 para finalizar: "))
        suma.append(numero)
    
    return sum(suma)
    
print(suma_hasta_cero())


    
    
