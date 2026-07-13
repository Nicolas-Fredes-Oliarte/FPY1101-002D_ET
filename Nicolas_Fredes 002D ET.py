print("====== cine max ======".upper())
print("")

peliculas = {
    "P101" : ["luz de Otoño", "drama", 110, "B", "Español", False],
    "P102" : ["Noche Neon", "accion", 125, "C", "Ingles", True],
    "P103" : ["Planeta Agua", "documental", 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'cienciaficción', 132, 'B', 'Ingles', False],
    }
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

def validar_entero(msg:str) -> int:
    while(True):
        try:
            valor = int(input(msg))

            if valor < 0:
                print("solo puede ingresar numeros enteros positivos".upper())
            else:
                return valor
        except Exception:
            print("solo puede ingresar numeros enteros positivos".upper())

def validar_caracter(msg:str) -> str:
    while(True):

        texto = input(msg)

        if len(texto) == 0:
            print("el texto no puede quedar vacio".upper())
        else:
            return texto
        
def validar_codigo(msg:str) -> int:
    while(True):
        codigo = input(msg)

        if len(codigo) == 0:
            print("el codigo no puede quedar vacio".upper())
        elif len(codigo) < 4:
            print("el codigo no puede contener menos de 4 carcateres".upper())
        elif len(codigo) > 4:
            print("el codigo no puede contener mas de 4 caracteres".upper())
        else:
            return codigo
        
def validar_texto_para_agregar(msg:str) -> str:
    while(True):

        texto = input(msg)

        if len(texto) == 0:
            print("el texto no puede quedar vacio".upper())
        elif texto.replace(" ","") == (""):
            print("el texto no puede quedar con espacios en blanco".upper())
        else:
            return texto
        
def validar_clasificacion(msg:str) -> str:
    while(True):

        clasificacion = input(msg)

        if len(clasificacion) == 0:
            print("el texto no puede quedar vacio".upper())
        elif (clasificacion != "A") and (clasificacion != "B") and (clasificacion != "C"):
            print("para clasificar una pelicula debe utilizar: [A - B - C] y en mayuscula".upper())
        else:
            return clasificacion
        
def genero_cupo(diccionario1:dict, diccionario2:dict):

    genero = validar_caracter("ingrese el genero de la pelicula para ver el cupo de entradas: ".upper())

    for i in diccionario1:
        if diccionario1[i][1] == genero:
            print(diccionario1[i])
            print(diccionario2[i])
            print("")

def buscar_pelicula_por_rango_de_precio(diccionario1:dict, diccionario2:dict):
    precio_minimo = validar_entero("ingrese el precio minimo que busca en una pelicula: ".upper())
    precio_maximo = validar_entero("ingrese el precio maximo que busca en una pelicula: ".upper())
    print("")

    for i in diccionario1:
        if diccionario2[i][0] > precio_minimo and diccionario2[i][0] < precio_maximo:
            print(diccionario1[i])
            print(diccionario2[i])
            print("")

def actualizar_precio(diccionario1:dict, diccionario2: dict):

    codigo_pelicula = validar_codigo("ingrese el codigo de la pelicula que desea actualizar: ".upper())
    
    for i in diccionario1:
        if i == codigo_pelicula:
            nuevo_precio = validar_entero("ingrese el nuevo precio de la pelicula: ".upper())
            diccionario2[i][0] = nuevo_precio
            print("precio actualizado".upper())
            print("")
            return None
    print("el codigo de la pelicula no existe".upper())
    return None

def agregar_pelicula(diccionario1:dict, diccionario2: dict):
    codigo_pelicula = validar_codigo("ingrese el codigo de la pelicula: ".upper())

    for i in diccionario1:
        if i == codigo_pelicula:
            print("el codigo de la pelicula ya existe".upper())
            print("")
            titulo_pelicula = validar_texto_para_agregar("ingrese el titulo de la pelicula: ".upper())
            genero_peliucla = validar_texto_para_agregar("ingrese el genero de la pelicula: ".upper())
            duracion_pelicula = validar_entero("ingrese la duracion de la pelicula: ".upper())
            clasificacion_pelicula = validar_clasificacion("ingrese la clasificacion de la peliucla: ".upper())
            idioma_pelicula = validar_texto_para_agregar("ingrese el idioma que esta disponible la pelicula: ".upper())
            while(True):
                formato_3D = validar_texto_para_agregar("la pelicula esta disponible para formato 3D? (s/n): ".upper())
                if formato_3D == "S" or formato_3D == "s":
                    formato_3D = True
                    break
                elif formato_3D == "N" or formato_3D == "n":
                    formato_3D = False
                    break
                else:
                    print("opcion invalida, las opciones validas son (s/n)".upper())
            precio_pelicula = validar_entero("ingrese el precio de la pelicula: ".upper())
            cupo_pelicula = validar_entero("ingrese la cantidad de cupos que tiene la pelicula: ".upper())

            lista1 = [titulo_pelicula, genero_peliucla, duracion_pelicula, clasificacion_pelicula, idioma_pelicula, formato_3D]
            lista2 = [precio_pelicula, cupo_pelicula]

            diccionario1[codigo_pelicula] = lista1
            diccionario2[codigo_pelicula] = lista2
            print("")
            print("pelicula agregada".upper())
            print("")
            break

def eliminar_pelicula(diccionario1:dict, diccionario2:dict):

    codigo_pelicula = validar_codigo("ingrese el codigo de la pelicula que desea eliminar: ".upper())

    for i in diccionario1:
        if i == codigo_pelicula:
            diccionario1.pop(i)
            diccionario2.pop(i)
            print("pelicula eliminada exitosamnete".upper())
            print("")
            return None
    print("el codigo de la pelicula no existe".upper())
    return None

def menu():
    while(True):
        print("=== menu principal ===".upper())
        print("")
        print("[1] - cupos por genero".upper())
        print("[2] - busqueda de peliculas por rango de precio".upper())
        print("[3] - actualizar precio de la pelicula".upper())
        print("[4] - agregar pelicula".upper())
        print("[5] - eliminar pelicula".upper())
        print("[6] - salir del programa".upper())
        print("")

        opc = validar_entero("ingrese una opcion: ".upper())
        print("")

        if opc == 1:
            print("opcion [1] cupos por genero".upper())
            print("")

            genero_cupo(peliculas, cartelera)

        elif opc == 2:
            print("opcion [2] busqueda de peliculas por rango de precio".upper())
            print("")

            buscar_pelicula_por_rango_de_precio(peliculas, cartelera)

        elif opc == 3:
            print("opcion [3] actualizar el precio de la pelicula".upper())
            print()

            actualizar_precio(peliculas, cartelera)

        elif opc == 4:
            print("opcion [4] agregar pelicula".upper())
            print("")

            agregar_pelicula(peliculas, cartelera)

        elif opc == 5:
            print("opcion [5] eliminar pelicula".upper())
            print("")

            eliminar_pelicula(peliculas, cartelera)

        elif opc == 6:
            print("opcion [6] salir del programa".upper())
            print("")

            print("cerrando programa, gracias por su preferencia".upper())
            print("")
            break

        else:
            print("opcion invalida, solo puede ingresar [1 - 2 - 3 - 4 - 5 - 6]".upper())
            print("")

menu()