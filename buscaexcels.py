import os
import pandas as pd

def buscar_archivos_excel(directorio):
    # Lista para almacenar los archivos encontrados
    archivos_excel = []
    
    # Recorremos el directorio en busca de archivos .xlsx
    for archivo in os.listdir(directorio):
        if archivo.endswith('.xlsx'):
            archivos_excel.append(archivo)
    
    return archivos_excel

def mostrar_menu(archivos_excel):
    print("Archivos Excel encontrados:")
    for i, archivo in enumerate(archivos_excel):
        print(f"{i + 1}. {archivo}")

def seleccionar_archivo(archivos_excel):
    while True:
        try:
            opcion = int(input("\nElige un archivo para abrir (número): "))
            if 1 <= opcion <= len(archivos_excel):
                return archivos_excel[opcion - 1]
            else:
                print("Opción inválida, por favor selecciona un número válido.")
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")

def abrir_excel(archivo):
    try:
        df = pd.read_excel(archivo)
        print("\nEl archivo se ha cargado correctamente. Aquí están las primeras filas:\n")
        print(df.head())
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")

def main():
    directorio = input("Introduce la ruta del directorio donde buscar archivos Excel: ")

    # Buscar archivos Excel en el directorio
    archivos_excel = buscar_archivos_excel(directorio)

    if archivos_excel:
        # Mostrar el menú con los archivos encontrados
        mostrar_menu(archivos_excel)
        
        # Seleccionar un archivo
        archivo_seleccionado = seleccionar_archivo(archivos_excel)
        print(f"\nHas seleccionado el archivo: {archivo_seleccionado}")
        
        # Abrir el archivo seleccionado
        ruta_archivo = os.path.join(directorio, archivo_seleccionado)
        abrir_excel(ruta_archivo)
    else:
        print(f"No se encontraron archivos Excel en el directorio: {directorio}")

if __name__ == "__main__":
    main()
