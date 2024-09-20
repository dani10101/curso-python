"""
base_de_datos_users= {1:"dani",2:"antonio"} 
base_de_datos_passwords ={1:"abc123",2:"abc321"}
print(base_de_datos_users.items())
print(base_de_datos_passwords)
usuario=input("introduce tu user")

if usuario in base_de_datos_users.values():
    password=input(f"introduce tu password para el usuario {usuario}")
    if password == base_de_datos_passwords.get(1):
        print("Bienvenido")


    
#if password in base_de_datos_passwords.values():
    #if base_de_datos_users.get(1)==base_de_datos_passwords.get(1):
     #   print("Bienvenido")
     """
base_de_datos={1:{"user":"dani","contraseña":"1234"},2:{"user":"antonio","contraseña":"234"}}
user=input("introduce un usuario")
contraseña=input("introduce una contraseña")
for datos in base_de_datos.values():
    if datos["user"]==user and datos["contraseña"]==contraseña:
        print("acceso concedido")

    
