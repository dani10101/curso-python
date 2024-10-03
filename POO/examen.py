class MiClase:
    @classmethod
    def mi_metodo(cls):
        suma = lambda x, y: x + y
        return suma(1, 2)

print(MiClase.mi_metodo())
suma_agregada = lambda n1, n2, n3: n3.append(n1 + n2)
print(suma_agregada)