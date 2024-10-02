from abc import ABC

class PersonaAcademica(ABC):  # Intefaz
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

class Alumno(PersonaAcademica):
    def __init__(self, nombre: str, edad: int, *, delegado: bool = False):
        super().__init__(nombre, edad)
        self.notas = []
        self.es_delegado = delegado

    def estudiar(self):
        ultima_nota = self.notas[-1] if self.notas else None
        if not ultima_nota or ultima_nota < 5:
            print("El alumno esta estudiando muy duramente, ya que esta motivado")
        else:
            print("El alumno esta estudiando")

class Profesor(PersonaAcademica):
    def __init__(self, nombre: str, edad: int, salario: float):
        super().__init__(nombre, edad)
        self.salario = salario

    @staticmethod
    def impartir_clase():
        print("El profesor esta impartiendo clase")

    @staticmethod
    def asignar_delegado_de_clase(alumno: Alumno):
        if alumno.es_delegado:
            print("El alumno ya es delegado de clase")
        else:
            alumno.es_delegado = True
            print(f"El alumno {alumno.nombre} se ha convertido en delegado de clase")

    @staticmethod
    def puntuar_alumno(alumno: Alumno, nota: int):
        alumno.notas.append(nota)

class Aula:
    def __init__(self, nombre: str, capacidad: int, profesor: Profesor, *, alumnos: Alumno = []):
        self.nombre = nombre
        self.capacidad = capacidad
        self.alumnos = alumnos
        self.profesor = profesor

    def alistar_alumno(self, alumno: Alumno) -> None|str:
        if len(self.alumnos) < self.capacidad:
            self.alumnos.append(alumno)
        else:
            raise ValueError("Esta clase esta completa y no se pueden alistar mas alumnos")
        
def gestionar_alumnos(aula: Aula, lista_alumnos: list[Alumno]) -> int:
    bucle_crear_alumnos = True
    while bucle_crear_alumnos:
        eleccion = input("Quieres crear un alumno?")
        if eleccion.lower() in ("no", "n"):
            bucle_crear_alumnos = False
        else:
            crear_alumno()
    print(f"Se van a anadir {len(lista_alumnos)} alumnos al aula {aula.nombre}")
    print(f"A esa aula le queda una capacidad de {aula.capacidad - len(aula.alumnos)}")
    alumnos_alistados = 0
    try:
        for alumno in lista_alumnos:
            aula.alistar_alumno(alumno)
    except ValueError:
        print("Se ha llegado al limite de alumnos para esta aula")
    print(f"Se han alistado {alumnos_alistados} alumnos")
    return alumnos_alistados

def crear_alumno() -> Alumno:  # Esto es una fabrica
    nombre = input("Dime el nombre del alumno: ")
    edad = input("Dime la edad del alumno: ")
    return Alumno(nombre, edad)