# Crear una baraja y barajarla
import random

figuras = ('Corazones', 'Diamantes', 'Tréboles', 'Picas')
valores = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey')
class Carta:
    def __init__(self, valor: str, figura: str):
        self.valor = valor
        self.figura= figura
    def __str__(self):
        return f"{self.valor} de {self.figura}"
        
    

class Baraja:
    def __init__(self):
        self.cartas = [Carta(valor, figura) for figura in figuras for valor in valores]

    def barajar(self):
        random.shuffle(self.cartas)
        print("Se ha barajado la baraja")

    def repartir(self, num_cartas: int):
        if num_cartas > len(self.cartas):
            print("No hay suficientes cartas para repartir")
            return []

        # Repartir el número de cartas solicitado
        cartas_repartidas = [self.cartas.pop() for _ in range(num_cartas)]
        return cartas_repartidas

    def mostrar(self):
        for carta in self.cartas:
            print(carta)

# Uso del código
baraja = Baraja()  # Crear la baraja
baraja.barajar()  # Barajar la baraja

# Repartir dos cartas
cartas_repartidas = baraja.repartir(2)

print("\nCartas repartidas:")
for carta in cartas_repartidas:
    print(carta)

