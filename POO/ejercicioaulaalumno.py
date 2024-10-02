"""1 - Hacer bien al Alumno
2 - Hacer bien al Aula
3 - Comprobar que se pueden asignar Alumnos al Aula
4 - Hacer una funcion que haga Alumnos
5 - Hacer que la funcion tome correctamente un Aula
6 - Asignar ALumnos recien creados a un Aula particular"""

class Alumno:

    def __init__(self,nombre:str,apellidos:str,lista_alumnos:list) -> None:
        self.nombre=nombre
        self.apellidos=apellidos
        lista_alumnos=lista_alumnos
    def crear_alumno():
        opcion_crear_alumno=input("quiere crear un alumno nuevo")
        if opcion_crear_alumno == "s":
            Alumno.nombre = input("Dime el nombre del alumno: ")
            Alumno.apellidos = input("Dime el apellido del alumno: ")
        else:
            pass

     
#3 tipos de aula segun su capacidad grande(50),mediana(30),pequeña(15)
class Aula:
    def __init__(self,nombre:str,capacidad:int,letras:dict,lista_alumnos_clasea:list,lista_alumnos_claseb:list
                 ,lista_alumnos_clasec:list) -> None:
        self.nombre=nombre
        self.capacidad=capacidad
        self.letras=letras
        self.lista_alumnos_clasea=lista_alumnos_clasea
        self.lista_alumnos_claseb=lista_alumnos_claseb
        self.lista_alumnos_clasec=lista_alumnos_clasec
    def crear_aula(**letras): 
          # Esto es una fabrica
        Aula.nombre = input("Dime el nombre de la clase: ")
        Aula.capacidad   = int(input("Dime la capacidad de la clase:15,30 o 50 "))
            
    def añadir_alumno_a_clase():
        lista_alumnos=[]
        lista_alumnos.append(Alumno.nombre)
        print("la lista de alumnos ha sido actualizada: ",lista_alumnos)
        if len(lista_alumnos) < 15 :
            lista_alumnos_clasea=[]
            lista_alumnos_clasea.append(Alumno.nombre)
            print("la lista de alumnos de la clase a es: ",lista_alumnos_clasea)
            


Alumno.crear_alumno()
Aula.crear_aula(letra_a=15,letra_b=30,letra_c=50)
Aula.añadir_alumno_a_clase()



""""

def gestionar_alumnos(aula: Aula, lista_alumnos: list[Alumno.nombre]) -> int:
    bucle_crear_alumnos = True
    while bucle_crear_alumnos:
        eleccion = input("Quieres crear un alumno?")
        if eleccion.lower() in ("no", "n"):
            bucle_crear_alumnos = False
        else:
            Alumno.crear_alumno()
    print(f"Se van a anadir {len(lista_alumnos)} alumnos al aula {aula.nombre}")
    print(f"A esa aula le queda una capacidad de {aula.capacidad - len(aula.lista_alumnos)}")
    alumnos_alistados = 0
    try:
        for alumno in lista_alumnos:
            aula.alistar_alumno(alumno)
    except ValueError:
        print("Se ha llegado al limite de alumnos para esta aula")
    print(f"Se han alistado {alumnos_alistados} alumnos")
    return alumnos_alistados

"""
