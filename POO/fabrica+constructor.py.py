from abc import ABC,abstractmethod



class Animales(ABC):
    
    @abstractmethod
    def ladrar():
        print("mi perrillo sigue ladrando")
    @abstractmethod
    def andar():
        print("el animal anda con dos patas" )
    @abstractmethod
    def nadar():
        print("el animal esta nadando")
    @abstractmethod
    def volar():
         print("el animal vuela")

class Perro:
        def __init__(self,nombre,edad):
            self.nombre=nombre
            self.edad=edad
           
        def __str__(self):
            return f"el perro con nombre: {self.nombre} y de edad: {self.edad}"

def fabrica(**args, objeto: object) -> object:
    try:
        return objeto(**args)
    except TypeError:
        raise ValueError("Argumentos incorrectos para esta clase")
try:
    diccionario={"nombre":"Jagguer","edad":3}
    perro=fabrica({"nombre"="Jagguer","edad"=3},objeto=Perro)
    print(perro)
    perro_invalido=fabrica("Jagger","dos",objeto=Perro)
except ValueError as e:
        print(e)
Animales.ladrar()

def fabrica1(*args, objeto: object) -> object:
    try:
        return objeto(*args)
    except TypeError:
        raise ValueError("Argumentos incorrectos para esta clase")
try:
    perro1=fabrica1("Jagger",3,objeto=Perro)
    print(perro1)
    perro1_invalido=fabrica1("Jagger","dos",objeto=Perro)
except ValueError as e:
        print(e)
Animales.ladrar()

