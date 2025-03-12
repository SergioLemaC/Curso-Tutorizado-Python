midiccionario = {"Alemania" : "Berlín",
                 "Francia" : "París",
                 "Reino Unido" : "Londres",
                 "España" : "Madrid"}

print(midiccionario["Francia"])

#Agregar elementos a un diccionario
midiccionario["Italia"] = "Lisboa"

#Modificar elementos
print(midiccionario)

midiccionario["Italia"] = "Roma"

print(midiccionario)

#Eliminar un elemento
del midiccionario["Reino Unido"]

print(midiccionario)

#Diferentes clave-valor
midiccionario2 = {"Alemania" : "Berlín",
                  23 : "Jordan",
                  "Mosqueteros" : 3}

#Utilizar una tupla para asignar las claves a los valores
mitupla = ("España", "Francia", "Reino Unido", "Alemania")

midiccionario3 = {mitupla[0] : "Madrid",
                  mitupla[1] : "París",
                  mitupla[2] : "Londres",
                  mitupla[3] : "Berlín"}

#Diccionario almacenando tupla
midiccionario4 = {23 : "Jordan",
                  "Nombre" : "Michael",
                  "Equipo" : "Chicago",
                  "Anillos" : [1991, 1992, 1993, 1996, 1997, 1998]}

print(midiccionario4["Anillos"])

#Diccionario dentro de otro
midiccionario5 = {23 : "Jordan",
                  "Nombre" : "Michael",
                  "Equipo" : "Chicago",
                  "Anillos" : {"Temporadas" : [1991, 1992, 1993, 1996, 1997, 1998]}}

print(midiccionario5["Anillos"])

#Claves del diccionario
print(midiccionario5.keys())

#Valores del diccionario
print(midiccionario5.values())

#Longitud del diccionario
print(len(midiccionario5))