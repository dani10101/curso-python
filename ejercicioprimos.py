# Guardando numeros primos en una lista
#version primera
""""
n=1
divisor = 2
primo = 0
prueba = n % divisor
if prueba == 0:
    primo = primo +1
    divisor = divisor +1
else:
    divisor = divisor +1
while n ==divisor:
    break
if primo == 0:
    print(n,"es primo")
else:
    print(n," no es primo")
"""
#primera version con un numero

#numeros = [3,2,8,7,4]

# Pedimos al usuario el rango de inicio y final
inicio = int(input("Introduce el número de inicio: "))
final = int(input("Introduce el número final: "))

# Generamos la lista de números a partir del rango
numeros = list(range(inicio, final + 1))  # Creamos la lista desde 'inicio' hasta 'final'

# Iteramos sobre cada número en la lista
for n in numeros:
    es_primo = True  
    divisor = 2 
    
    # Verificamos si el número es mayor que 1, ya que 1 no es primo
    if n > 1:
        # Empezamos el ciclo desde el divisor 2 hasta la raíz cuadrada de n
        while divisor * divisor <= n:
            if n % divisor == 0:
                es_primo = False  # Si encontramos un divisor, no es primo
                break
            divisor += 1

    # Imprimimos si el número es primo o no
    if es_primo and n > 1:
        lista = [n]
        print(lista)
    



    
        

