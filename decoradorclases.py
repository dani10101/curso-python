from dataclasses import dataclass, field
@dataclass
class Personaje:#clase padre
    nombre : str
    rol :str
    puntos_vida : int = 100
    inventario :list = field(default_factory=list)
    nivel :int = 1
    damage: list = field(default_factory=list)
    def __post_init__(self):
        print(f"Se ha creado a {self.nombre}, un {self.rol} de nivel {self.nivel}! con {self.puntos_vida} puntos de vida")

class Guerrero(Personaje):#clase hija
    def __init__(self, nombre,rol):
        super().__init__(nombre,rol)
        



class Mago(Personaje):#clase hija
    def __init__(self, nombre,rol):
        super().__init__(nombre,rol)
        

class cualidades(Personaje):#clase hija
    def __init__(self, nombre):
        super().__init__(nombre)#hereda todas las instancias o atributos del constructor de la clase padre
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