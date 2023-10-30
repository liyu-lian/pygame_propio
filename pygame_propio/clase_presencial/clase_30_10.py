#CLase de hoy: diccionario
from copy import deepcopy

""" Los nombres de las claves deben estar en español, además de tener sus nombres completos 
☻ diccionario = {'nombre' = 'Tiara'}
☺ diccionario =  {'nm' = 'rosy'}"""

diccionario = {"nombre": "Juliana", "estudios": {"carrera": "Técnico en programación", "año": 2023}}

""" for clave in diccionario:
    if (type(diccionario[clave]) == dict):
        for clave_dos in diccionario[clave]:
            print(diccionario[clave][clave_dos])
    else:
        print(diccionario[clave]) """

#estoy tomando el mismo diccionario, por lo tanto estoy editando el original también
""" diccionario_2 = diccionario
diccionario_2["nombre"] = "Ale"

print(diccionario)
print(diccionario_2)

print(id(diccionario))
print(id(diccionario_2)) """

# print(diccionario["estudios"])

#EXISTEN DOS FORMAS DE COPIAR UN DICCIONARIO

""" 
    ♥ Shallow Copy: Modifica solamente la informacion del diccionario, pero una lista o diccionario anidado no lo va a modificar 

diccionario_2 = diccionario.copy()
diccionario_2["estudios"]["año"] = 2021

print(diccionario)
print(diccionario_2)

print(id(diccionario))
print(id(diccionario_2))
"""

""" DEEP COPY:  Debe importarse deepcopy. From copy import deepcopy. 
        ○ Es capaz de hacer una copia editable aùn con diciconarios anidados

diccionario_2 = deepcopy(diccionario)
diccionario_2["estudios"]["año"] = 2021

print(diccionario)
print(diccionario_2)

print(id(diccionario))
print(id(diccionario_2))
"""

#  GET()

""" nombre = diccionario.get("legajo", "No se pudo acceder a la clave") #No rompe el código si la clave no existe. Solo devuelve NONE o el mensaje ingresado
#legajo = diccionario["legajo"] --> Aquí se rompe el código si lo ejecutamos

print(nombre)
"""
# KEYS

""" #No se puede modificar a no ser que se use un split para obtener las keys
claves = list(diccionario.keys()) # se transforma a lista para hacerlo mosificable

print(type(claves)) """

""" #VALUES: Muesra los valores dentro de las keys
for valores in diccionario.values():
    print(valores) """

#metodo items: devuelve clave y valor

""" print(list(diccionario.items())[0]) """

#POP: ELIMINA LA CLAVE Y EL VALOR

""" nombre = diccionario.pop("legajo","No existe")
print(nombre)
print(diccionario) """

#UPDATE: editar la clave de un diccionario

diccionario.update({"nombre": 11111})
print(diccionario)

