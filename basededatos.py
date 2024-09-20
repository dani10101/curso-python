base_de_datos={1:{"user":"dani","contraseña":"1234"},2:{"user":"antonio","contraseña":"234"}}
user=input("introduce un usuario")
contraseña=input("introduce una contraseña")
for datos in base_de_datos.values():
    if datos["user"]==user and datos["contraseña"]==contraseña:
        print("acceso concedido")

    
