import tkinter as tk
import webbrowser

# Función para abrir el navegador con la búsqueda
def buscar():
    # Obtener el término de búsqueda del cuadro de texto
    termino = entrada.get()
    
    # URL de búsqueda en Google con el término ingresado
    url = f"https://www.google.com/search?q={termino}"
    
    # Abrir la URL en el navegador predeterminado
    webbrowser.open(url)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Buscador en Navegador")

# Etiqueta para indicar el cuadro de búsqueda
etiqueta = tk.Label(ventana, text="Buscar en Google:")
etiqueta.pack(pady=10)

# Cuadro de texto para ingresar la búsqueda
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=5)

# Botón para realizar la búsqueda
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar)
boton_buscar.pack(pady=10)

# Ejecutar el loop principal de la interfaz
ventana.mainloop()
