def agenda():
     
    agenda ={}
    contacto=input("introduce un nombre de contacto")
    agenda={"contacto":contacto}
    numero=input("introduce un numero")
    agenda["numero"]= numero
    print(agenda)
agenda()