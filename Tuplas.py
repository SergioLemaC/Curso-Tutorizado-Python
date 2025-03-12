#Sintaxis de las tuplas

#nombre_tupla = (elem1, elem2, elem3...) los paréntesis son opcionales

mitupla = ("Juan", 13, 1, 1995)

#Acceder a un elemento en concreto
print(mitupla[2])

#Convertir tupla a lista
milista = list(mitupla)

#print(milista)

#print(mitupla)

#Convertir lista en tupla
milista2 = ["Juan", 13, 1, 1995]

mitupla2 = tuple(milista2)

print(mitupla2)

#Para saber si existe ese elemento en la tupla
print("Juan" in mitupla2)

#Cuantas veces está un elemento dentro de la tupla
print(mitupla2.count("Juan"))

#Longitud de una tupla
print(len(mitupla2))

#Desempaquetado de tuplas, extraer los datos y asignarlos a las variables
nombre, dia, mes, año = mitupla2

print(nombre)
print(dia)
print(año)
print(mes)