def almacen():    
    acceso_concedido=False
    base_de_datos={"1":{"user":"dani","contraseña":"1234"},"2":{"user":"antonio","contraseña":"234"}}
    #login
    while not acceso_concedido:
        usuario=input("usuario")
        contrasenia=input("password")
        for datos in base_de_datos.values():
            a=datos["user"]
            b=datos["contraseña"]
            while a==usuario and b==contrasenia:
                print("accceso concedido")
                #menu principal
                opcion=input("introduce una opcion: \n""1 Busca id\n"
                                        "2 Remueve usuarios\n"
                                        "3 Agrega usuarios\n"
                                        )
                
                if opcion=="1":
                #buscador de ids
                    id=input("introduce un id a buscar")
                    id=base_de_datos.get(id)
                    print(id)
                else:
                    print("el usuario con ese id no se ha encontrado")
                    
                if opcion=="3":
                    #solicitamos un ide nuevo
                    #menu 3 agregar usuarios
                    ide_nuevo=input("introduce un ide nuevo")
                    usuario_nuevo=input("introduce un user nuevo")
                    contra_nueva=input("introduce la contraseña para este usuario")
                    #declaro otra variable con nuevos datos items del diccionario para su actualizacion
                    nuevos_datos={ide_nuevo:{"user":usuario_nuevo,"contraseña":contra_nueva}}
                    base_de_datos.update(nuevos_datos)
                    print(base_de_datos)
                    

                elif opcion=="2":
                    #menu 2 remover usuarios nuevos
                    id_borrar=input("introduce el id del usuario que quieres borrar")
                    if id_borrar in base_de_datos.keys():
                        base_de_datos.pop(id_borrar,"usuario eliminado")
                        print(id_borrar)
                
            
                        
            

            else:
                print("usuario o clave incorrecta intentelo de nuevo")

almacen()               




        

            
                    
        



