conversion= lambda numero_hex: int(numero_hex,16)
def hex_string_to_rgb(string_hex: str)->dict:
    rojo,verde,azul = [string_hex[1:3],string_hex[3:5],string_hex[5:]]
    return {"r": conversion(rojo),"g": conversion(verde),"b": conversion(azul)}
print(hex_string_to_rgb("FF9913"))   