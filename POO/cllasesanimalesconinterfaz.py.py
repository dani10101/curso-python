from abc import ABC,abstractmethod

class Animales(ABC):
    def __init__(self,nombre:list):
        self.nombre=nombre
    
    def crear_animal():#esto es una fábrica
        nombre_animal=input("que animal quieres crear")
        if nombre_animal == "Perro":
              Animales.ladrar()
        if nombre_animal== "Pezvolador":
             Animales.nadar()
             Animales.volar()
        nombre=[]
        nombre.append(nombre_animal)
        print(nombre)
        opcion=input("desea fabricar otro animal")
        if opcion== "s":
             Animales.crear_animal()
        else:
             pass
        
    @abstractmethod
    def ladrar():
        print("el animal esta ladrando")
    @abstractmethod
    def andar():
        print("el animal anda con dos patas" )
    @abstractmethod
    def nadar():
        print("el animal esta nadando")
    def volar():
         print("el animal vuela")
class Pato(Animales):
        Animales.ladrar()
class Pezvolador(Animales):
        Animales.nadar()
        Animales.volar()
Animales.crear_animal()