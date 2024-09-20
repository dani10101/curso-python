numero=input("Dime un numero")
numero_str= str(numero)
if numero_str == numero_str[::-1]:
    total=0
    for numero in numero_str:
        total+= int(numero)
        print(total)
else:
    print("no es capicua")