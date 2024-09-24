string = "ab3nj2p15aab  3"

def eleva_cuadrado(string: str) -> list[int]:
    numeros = []
    for caracter in string:
        if caracter.isdigit():
            numeros.append(int(caracter) ** 2)
    return numeros

print(eleva_cuadrado(string))
