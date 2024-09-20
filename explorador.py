import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileExplorer(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Explorador de Archivos Personalizado")
        self.geometry("600x400")
        self.configure(bg="#282C34")  # Fondo oscuro

        # Etiqueta de título
        self.title_label = tk.Label(self, text="Explorador de Archivos", font=("Helvetica", 16), fg="#61AFEF", bg="#282C34")
        self.title_label.pack(pady=10)

        # Botón para abrir el explorador de archivos
        self.open_button = tk.Button(self, text="Abrir Archivo", command=self.open_file, font=("Helvetica", 12), bg="#61AFEF", fg="#282C34")
        self.open_button.pack(pady=10)

        # Botón para abrir el explorador de carpetas
        self.open_folder_button = tk.Button(self, text="Abrir Carpeta", command=self.open_folder, font=("Helvetica", 12), bg="#98C379", fg="#282C34")
        self.open_folder_button.pack(pady=10)

        # Caja de texto para mostrar la ruta seleccionada
        self.path_label = tk.Label(self, text="Ruta seleccionada:", font=("Helvetica", 12), fg="#E06C75", bg="#282C34")
        self.path_label.pack(pady=20)

        self.path_text = tk.Text(self, height=2, width=60, wrap="word", bg="#1E1E1E", fg="white", font=("Helvetica", 10))
        self.path_text.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Seleccionar Archivo")
        if file_path:
            self.path_text.delete(1.0, tk.END)
            self.path_text.insert(tk.END, file_path)
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

    def open_folder(self):
        folder_path = filedialog.askdirectory(title="Seleccionar Carpeta")
        if folder_path:
            self.path_text.delete(1.0, tk.END)
            self.path_text.insert(tk.END, folder_path)
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ninguna carpeta.")

if __name__ == "__main__":
    app = FileExplorer()
    app.mainloop()
