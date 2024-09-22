import tkinter as tk
import webbrowser

# Función para realizar la búsqueda con los operadores seleccionados
def buscar():
    # Obtener el término de búsqueda del cuadro de texto
    termino = entrada.get()

    # Construir la búsqueda con operadores
    operadores = []

    if var_index_of.get():
        operadores.append('"index of"')
    if var_site.get():
        operadores.append(f'site:{entrada_site.get()}')
    if var_filetype.get():
        operadores.append(f'filetype:{entrada_filetype.get()}')
    if var_intitle.get():
        operadores.append(f'intitle:{entrada_intitle.get()}')

    # Concatenar el término de búsqueda con los operadores seleccionados
    consulta = f"{termino} {' '.join(operadores)}"

    # URL de búsqueda en Google con el término y operadores
    url = f"https://www.google.com/search?q={consulta}"

    # Abrir la URL en el navegador predeterminado
    webbrowser.open(url)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Buscador Avanzado en Google")

# Etiqueta para indicar el cuadro de búsqueda
etiqueta = tk.Label(ventana, text="Buscar en Google:")
etiqueta.pack(pady=10)

# Cuadro de texto para ingresar el término de búsqueda
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=5)

# Checkbutton para incluir "index of" en la búsqueda
var_index_of = tk.BooleanVar()
check_index_of = tk.Checkbutton(ventana, text='Usar "index of"', variable=var_index_of)
check_index_of.pack(pady=2)

# Checkbutton y entrada para el operador "site:"
var_site = tk.BooleanVar()
check_site = tk.Checkbutton(ventana, text='Usar "site:"', variable=var_site)
check_site.pack(pady=2)
entrada_site = tk.Entry(ventana, width=30)
entrada_site.pack(pady=2)

# Checkbutton y entrada para el operador "filetype:"
var_filetype = tk.BooleanVar()
check_filetype = tk.Checkbutton(ventana, text='Usar "filetype:"', variable=var_filetype)
check_filetype.pack(pady=2)
entrada_filetype = tk.Entry(ventana, width=30)
entrada_filetype.pack(pady=2)

# Checkbutton y entrada para el operador "intitle:"
var_intitle = tk.BooleanVar()
check_intitle = tk.Checkbutton(ventana, text='Usar "intitle:"', variable=var_intitle)
check_intitle.pack(pady=2)
entrada_intitle = tk.Entry(ventana, width=30)
entrada_intitle.pack(pady=2)

# Botón para realizar la búsqueda
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar)
boton_buscar.pack(pady=10)

# Ejecutar el loop principal de la interfaz
ventana.mainloop()
