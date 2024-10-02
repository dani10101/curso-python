
def rgb(r, g, b):
    # Función para limitar el valor en el rango de 0 a 255
    def agrupar(value):
        return max(0, min(255, value))
    
    # Limitar los valores RGB
    r = agrupar(r)
    g = agrupar(g)
    b = agrupar(b)
    
    # Convertir a hexadecimal y formatear como dos dígitos
    return f"{r:02X}{g:02X}{b:02X}"

# Ejemplos de uso
print(rgb(255, 255, 255))  # "FFFFFF"
print(rgb(255, 255, 300))  # "FFFFFF"
print(rgb(0, 0, 0))        # "000000"
print(rgb(148, 0, 211))    # "9400D3"
