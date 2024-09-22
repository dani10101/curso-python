
string=input("dame un string")
string=string.lower()
if string[0]==string[-1]:
    print("si")
else:
    print("no")

# El usuario ingresa varios elementos separados por espacios
def es_palindromo(numero):
    return str(numero) == str(numero)[::-1]
 
# Ejemplo de uso
numero = 1001
resultado = es_palindromo(numero)
print(f"El número {numero} es palíndromo: {resultado}")
#validar numeros de telefonos:
lista_telefonos =input("introduce un telefono")
longitud = len(lista_telefonos)
telefono_limpio = lista_telefonos.replace(" "," ")
print(longitud)
if longitud == 9:
    print("es ok")





