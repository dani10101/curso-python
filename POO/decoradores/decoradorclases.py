from dataclasses import dataclass, field
@dataclass
class Personaje:#clase padre
    nombre : str
    rol :str
    puntos_vida : int = 100
    inventario :list = field(default_factory=list)
    nivel :int = 1
    damage: list = field(default_factory=list)
    def creacion(self):
        return f"Se ha creado a {self.nombre}, un {self.rol} de nivel {self.nivel}! con {self.puntos_vida} puntos de vida"
#@dataclass("Guts":str ,"guerrero":str)


class Asalariado:
    def __init__(self):
        self.nombre="DANIEL"
        self.salario=100
    def subir_salario():()
"""

class cualidades(Personaje):#clase hija
    
    def ataque_basico():
        print(gandalf.nombre,"ha atacado a ",guts.nombre)
        print(gandalf.nombre,"hace un daño de ",gandalf.damage)
    @staticmethod
    def vida():
        lista_damage_int=[int(i) for i in gandalf.damage]
        guts.puntos_vida-=lista_damage_int[0]
        print(guts.nombre ," tiene" ,guts.puntos_vida, "de vida")
#creacion de instancias
gandalf=Mago("Gandalf","mago")       
guts= Guerrero("Guts","guerrero")
# Ejecución de métodos
gandalf.damage.append(10)  # Añadir daño al mago
cualidades.ataque_basico()  # Realizar ataque básico
cualidades.vida()  # Reducir la vida de Guts
"""