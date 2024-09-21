
opcion=input("introduce una opcion: \n""1 Busca id\n"
                                    "2 Login\n"
                                    "3 Agrega usuarios")
base_de_datos={"1":{"user":"dani","contraseña":"1234"},"2":{"user":"antonio","contraseña":"234"}}
if opcion=="1":
    #buscador de ids
    id=input("introduce un id a buscar")
    id=base_de_datos.get(id)
    print(id)
elif opcion=="2":
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

elif opcion=="3":
    #solicitamos un ide nuevo
    ide_nuevo=input("introduce un ide nuevo")
    usuario_nuevo=input("introduce un user nuevo")
    contra_nueva=input("introduce la contraseña para este usuario")
    #declaro otra variable con nuevos datos items del diccionario para su actualizacion
    nuevos_datos={ide_nuevo:{"user":usuario_nuevo,"contraseña":contra_nueva}}
    base_de_datos.update(nuevos_datos)
    print(base_de_datos)









    

        
                
    



