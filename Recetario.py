from pathlib import Path
from os import system
import os

mi_ruta = "C:/Users/Jorge/Desktop/Python/Dia 6/Recetas"
def bienvenida():
    print("Bienvenido al recetario")
    print(f"Las recetas están en {mi_ruta}")

    contador = 0
    for txt in Path(mi_ruta).glob("**/*.txt"):
        contador +=1

    print(f"Hay {contador} recetas")

def mostrar_categorias():
    print("Categorias:")
    ruta_categorias = Path(mi_ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - [{carpeta_str}]")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def elige_categoria(lista):
    categoria = "x"

    while not categoria.isnumeric() or int(categoria) not in range(1, len(lista)+1):
        categoria = input("\nElige una categoria: ")

    return lista[int(categoria) -1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_receta = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_receta.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - [{receta_str}]")
        lista_recetas.append(receta)
        contador +=1

    return lista_recetas

def elige_receta(lista):
    eleccion_receta = "x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) +1):
        eleccion_receta = input("\nElige una receta: ")

    return lista[int(eleccion_receta) -1]


def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        nombre_receta = input("Escribe el nombre de tu receta: ") + ".txt"
        contenido_receta = input("Introduzca el contenido de la receta: ")
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Esa receta ya existe")


def eliminar_receta(receta):
    Path.unlink(receta)
    print(f"La receta {receta} ha sido eliminada")
def crear_categoria(ruta):
    existe = False

    while not existe:
        nombre_categoria = input("Escribe el nombre de la categoria: ")
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Esa categoria ya existe")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria} ha sido eliminada")


def menu():

    opcion = "x"
    while not opcion.isnumeric() or int(opcion) not in range(1,7):

        print("[1]-Leer receta [2]-Crear receta [3]-Crear categoria [4]-Eliminar receta "
              "[5]-Eliminar categoria [6]-Salir del programa")

        opcion = int(input("Introduzca una opcion: "))

        match opcion:
            case 1:
                mis_categorias = mostrar_categorias()
                categoria = elige_categoria(mis_categorias)
                mis_recetas = mostrar_recetas(categoria)
                if len(mis_recetas) < 1:
                    print("no hay recetas en esta categoría.")
                else:
                    receta = elige_receta(mis_recetas)
                    leer_receta(receta)

            case 2:
                mis_categorias = mostrar_categorias()
                categoria = elige_categoria(mis_categorias)
                crear_receta(categoria)

            case 3:
                crear_categoria(mi_ruta)

            case 4:
                mis_categorias = mostrar_categorias()
                categoria = elige_categoria(mis_categorias)
                mis_recetas = mostrar_recetas(categoria)
                if len(mis_recetas) < 1:
                    print("no hay recetas en esta categoría.")
                else:
                    receta = elige_receta(mis_recetas)
                    eliminar_receta(receta)

            case 5:
                mis_categorias = mostrar_categorias()
                categoria = elige_categoria(mis_categorias)
                if len(mostrar_recetas(categoria)) > 0:
                    print("\nHay recetas en esta categoría, para eliminar la categoría, "
                          "debes eliminar primero la receta.")
                else:
                    eliminar_categoria(categoria)

            case 6:
                break


        input("Presione cualquier tecla para volver al inicio: ")
        opcion = "x"
        system("cls")


bienvenida()
menu()



