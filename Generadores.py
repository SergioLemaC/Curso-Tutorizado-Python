#Función normalele
def genera_pares(limite):
    num = 1

    mi_lista = []

    while (num < limite):
        mi_lista.append(num * 2)
        num+=1
    
    return mi_lista

print(genera_pares(10))

#Función generadora
def generaPares(limite):
    num = 1

    while(num < limite):
        yield num * 2

        num+=1

devuelvePares = generaPares(10)

#for i in devuelvePares:
#    print(i)

print(next(devuelvePares)) #Devuelve el 1er valor que tiene almacenado

print("Aquí podría ir más código...")

#Es como un LazyLoading en Java
print(next(devuelvePares)) #Devuelve el 2do valor que tiene almacenado

#yield from
def devuelve_ciudades(*ciudades): # (*) Recibe un número indeterminado de elementos y son en forma de tuplas
    
    for elemento in ciudades:

        #for subElemento in elemento: yield from prescinde del bucle for anidado
        yield from elemento #Esto para recorrer el subelemento de cada elemento del array/tupla

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))