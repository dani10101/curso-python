class Personaje:#clase padre
    def __init__(self, nombre: str, rol: str,):
        self.nombre = nombre
        self.rol = rol
        self.puntos_vida = 100
        self.inventario = []
        self.nivel = 1
        self.damage=[]
        print(f"Se ha creado a {self.nombre}, un {self.rol} de nivel {self.nivel}! con estos  {self.puntos_vida} puntos de vida")
class Guerrero(Personaje):#clase hija
    def __init__(self, nombre,rol):
        super().__init__(nombre,rol)
        
guts= Guerrero("Guts","guerrero")


class Mago(Personaje):#clase hija
    def __init__(self, nombre,rol):
        super().__init__(nombre,rol)
        
gandalf=Mago("Gandalf","mago")
class cualidades(Personaje):#clase hija
    def __init__(self, nombre):
        super().__init__(nombre)#hereda todas las instancias o atributos del constructor de la clase padre
    def ataque_basico(nombre):
        
        print(gandalf.nombre,"ha atacado a ",guts.nombre)
        print(gandalf.nombre,"hace un daño de ",gandalf.damage)
    def vida():
        lista_damage_int=[int(i) for i in gandalf.damage]
        guts.puntos_vida-=lista_damage_int[0]
        print(guts.nombre ," tiene" ,guts.puntos_vida, "de vida")
        
        
cualidades.ataque_basico(gandalf.damage.append(10)) 
#ataque_gandalf=cualidades.ataque_basico(gandalf.damage.append(10))
cualidades.vida()

