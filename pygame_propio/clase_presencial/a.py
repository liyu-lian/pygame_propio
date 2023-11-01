lista_datos = \
[
    {"Nombre":"Juan", "Sexo":"M", "Edad":"24", "Pais":"Argentina"},
    {"Nombre":"Maria", "Sexo":"F", "Edad":"19", "Pais":"Mexico"},
    {"Nombre":"Rodrigo", "Sexo":"NB", "Edad":"20", "Pais":"Chil"},
    {"Nombre":"Beto", "Sexo":"M", "Edad":"27", "Pais":"Uruguay"},
    {"Nombre":"Hinata", "Sexo":"M", "Edad":"30", "Pais":"Japon"}
]

def listar_dato(lista: list):
    for persona in lista:
        nombre = persona.get("Nombre", "No se pudo obtener el dato")
        print(nombre)

def eliminar_key(lista: list):
    for persona in lista:
        nombre = persona.pop("Nombre", "No existe")

        print(persona)

def agregar_key(lista: list):
    for persona in lista:
        persona = persona.update({"País de origen": "Argentina"})

    print(persona)

dato = listar_dato(lista_datos)
print("\n"+ dato)