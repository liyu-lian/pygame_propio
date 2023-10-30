from os import system 

system("cls")
'''
CONSIGNA: Dado un conjunto de 5 habitantes default, y un menu con opciones,
programar las 3 funciones llamadas en este ultimo (1,2,3) 
para permitir el correcto funcionamiento de la app


.Entender el codigo base que se presenta y resolver las funcionalidades faltantes
.Aplicar correctamente los nuevos metodos vistos
.No preocuparse por 
    .lo atomicas y reutilizables que puedan ser las funciones}
    .Buenas practicas vistas en la materia (ej, 1 solo return x funcion, 
    verificar si dato es entero antes de castearlo, etc...)
'''

lista_datos = \
[
    {"Nombre":"Juan", "Sexo":"M", "Edad":"24", "Pais":"Argentina"},
    {"Nombre":"Maria", "Sexo":"F", "Edad":"19", "Pais":"Mexico"},
    {"Nombre":"Rodrigo", "Sexo":"NB", "Edad":"20", "Pais":"Chil"},
    {"Nombre":"Beto", "Sexo":"M", "Edad":"27", "Pais":"Uruguay"},
    {"Nombre":"Hinata", "Sexo":"M", "Edad":"30", "Pais":"Japon"}
]

def mostrar_diccionarios():
    for habitante in lista_datos:
        print(habitante)

def menu()->str:
    menuString = \
    '''
    0. Ver diccionarios hasta el momento
    1. () Listar un dato sobre todos los habitantes (por ejempo, todas las edades)
    2. () Eliminar una key de un diccionario específico (y mostrarla)
    3. () Agregar una key con su value a un diccionario específico
    4. Salir
    \n
    '''
    return menuString

def menu_funcionalidades():
    while True:
        print(menu())
        match(input("Ingrese un numero: (0), 1, 2, 3 o 4: ")) :
            case "0":
                print("\n")
                mostrar_diccionarios()
            case "1":
                caso_uno = listar_dato(lista_datos)
                print("\n" + caso_uno) # Para que no quede pegado al menu
            case "2":
                caso_dos = eliminar_key(lista_datos)
                print("\n" + caso_dos)
            case "3":
                caso_tres = agregar_key(lista_datos)
                print("\n" + caso_tres)
            case "4":
                break


def listar_dato(lista: list):
    lista_nombre = []

    for persona in lista:
        nombre = persona.get("Nombre", "No se pudo obtener el dato")

        lista_nombre.append(nombre)

    return str(lista_nombre)

def eliminar_key(lista: list):
    lista_copy = lista.copy()

    for persona in lista_copy:
        persona.pop("Nombre", "No existe")

    sin_nombre = lista

    return str(sin_nombre)

def agregar_key(lista: list):
    for persona in lista:
        persona = persona.update({"País de origen": "Argentina"})

    return str(lista)

menu_funcionalidades()

