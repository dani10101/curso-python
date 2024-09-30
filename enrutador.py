from functools import wraps

class Router:
    def __init__(self):
        self.routes = {}  # Aqui se guardan las rutas como pares metodo,ruta (clave): funcion (valor)

    def add_route(self, metodo: str, ruta: str, func: callable):
        self.routes[(metodo, ruta)] = func  # Se guardan tuplas UNICAS de metodo y ruta y un callback preparado

    def route(self, metodo: str, ruta: str):
        funcion_invocada = self.routes.get((metodo, ruta))  # Mira a ver si encuentra la ruta
        if funcion_invocada:
            return funcion_invocada
        else:
            return f"Error 404: {metodo} {ruta} no encontrado."


# Crear una instancia de Router
router = Router()

def route(metodo: str, ruta: str) -> callable:
    def decorador(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        router.add_route(metodo, ruta, wrapper)
        return wrapper
    return decorador

# Ejemplo de uso
@route('POST', '/mi_ruta_post')
def mi_funcion_post(usuario):
    return f"Has subido el usuario {usuario}"

# Probar las rutas
usuario = input("Dame un usuario: ")
llamada = router.route('POST', '/mi_ruta_post')
print(llamada(usuario))