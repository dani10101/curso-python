import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Función para dibujar cubos pequeños
def dibujar_cubo(ax, pos, color):
    # Definir los vértices de un cubo
    r = [0, 1]
    vertices = [[x, y, z] for x in r for y in r for z in r]
    
    # Trasladar el cubo a la posición deseada
    vertices = [[v[0] + pos[0], v[1] + pos[1], v[2] + pos[2]] for v in vertices]

    # Definir las caras del cubo
    caras = [[vertices[j] for j in [0, 1, 3, 2]],
             [vertices[j] for j in [4, 5, 7, 6]],
             [vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [2, 3, 7, 6]],
             [vertices[j] for j in [0, 2, 6, 4]],
             [vertices[j] for j in [1, 3, 7, 5]]]
    
    # Crear el cubo y asignar color
    ax.add_collection3d(Poly3DCollection(caras, facecolors=color, linewidths=1, edgecolors='black', alpha=0.9))

# Función para crear el cubo de Rubik completo
def dibujar_cubo_rubik():
    # Crear la figura y los ejes 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Definir los colores típicos de un cubo de Rubik
    colores = {
        'blanco': 'white', 'amarillo': 'yellow', 'rojo': 'red', 
        'naranja': 'orange', 'verde': 'green', 'azul': 'blue'
    }
    
    # Dibujar los 27 cubos pequeños (3x3x3)
    for x in range(3):
        for y in range(3):
            for z in range(3):
                # Asignar color según la posición en cada cara
                color = [colores['blanco'], colores['verde'], colores['rojo'], colores['amarillo'], colores['azul'], colores['naranja']]
                # Dibujar cada cubo pequeño
                dibujar_cubo(ax, (x, y, z), color)
    
    # Configurar los límites y ángulos de la gráfica
    ax.set_xlim([0, 3])
    ax.set_ylim([0, 3])
    ax.set_zlim([0, 3])
    ax.view_init(30, 30)  # Ángulo de vista
    plt.show()

# Llamar a la función para dibujar el cubo de Rubik
dibujar_cubo_rubik()
