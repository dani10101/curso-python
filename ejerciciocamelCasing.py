def solution(s: str) -> str:
    #almaceno el resukltado en una lista
    result = []
    #iteramos sobre el string
    for char in s:
       #hasta que encuentre una mayuscula
        if char.isupper():
            result.append(' ')#añade un espacio a resultado
        
       #añade el resto del string a resultado
        result.append(char)
    
    #devuelve espacio concatenado con resultado
    return ''.join(result)

print(solution("HoLaMundo"))
