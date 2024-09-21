base_de_datos={1:{"user":"dani","contraseña":"1234"},2:{"user":"antonio","contraseña":"234"}}
acceso_concedido=False
while not acceso_concedido:
    usuario=input("usuario")
    contrasenia=input("password")
    for datos in base_de_datos.values():
        a=datos["user"]
        b=datos["contraseña"]
        if a==usuario and b==contrasenia:
            print("accceso concedido")
            acceso_concedido=True
    if not acceso_concedido:
        print("usuario o clave incorrecta intentelo de nuevo")


    
    
        
                
    



