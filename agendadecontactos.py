#hacer una funcion para anotar contactos y numeros en una agenda
#hacer un menu que la primera opcion sea añadir contacto,la segunda sea eliminar contacto y la tercera
#sea salir del programa.
#si no hay contactos ejecutar menu principal de forma infinita.

def agenda():
    agenda={}
    opciones=          input ("1.añadir contacto\n"
                        "2.eliminar contacto\n"
                        "3.salir\n"
                        "4.menu principal")
    
    print("2.eliminar contacto")
    print("3 salir")
    #incluir inputs para seleccionar opciones
    opciones = input("introduce una opcion 1 ,2 o 3: ")
    #ejecutamos un bucle condicional para verificar la opcion 1
    while opciones == "1":
        contacto=input("introduce un nombre de contacto")#es un elemento de agenda que posteriormente añadiré
        numero=input("introduce un numero de telefono")
        agenda["contacto"]= contacto
        agenda.update({"numero":numero})
        opciones= input("desea salir de este menu s o n")
        opciones="s"
    
        
agenda()