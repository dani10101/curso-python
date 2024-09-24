estudiantes = [("Alicia", 25), ("Joaquin", 20), ("Carlos", 23), ("David", 22)]
ordenar_por_edad = lambda estudiante: estudiante[1]  # Que es la posicion de la edad
estudiantes.sort(key=ordenar_por_edad)  # Se le da la funcion como argumento para ordenar (callback)
print(estudiantes)

var = lambda num1, num2 : num1 + num2
print(var(4,7))

#casteo datos string a int
lista_strings = ['1', '2', '3', '4', '5']
lista_enteros = list(map(int, lista_strings))
print(lista_enteros)
lista_datos_string=[]
datos=input("introduce numeros separados por , ")
lista_datos_integers=[int(n) for n in lista_datos_string]
lista_datos_integers.append(datos)
print(lista_datos_integers)

#usando comprension de listas
lista_strings = ['1', '2', '3', '4', '5']
lista_enteros = [int(i) for i in lista_strings]

