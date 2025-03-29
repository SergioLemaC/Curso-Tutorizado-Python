#Sintaxis de las listas

#nombre_lista = [elem1, elem2, elem3]

mi_lista = ["María", 5, True, 78.35]

#Imprimir la lista completa
print(mi_lista[:])

#Acceder a un elemento en concreto
print(mi_lista[2]) #Marta

#Si colocamos un número negativo cuenta la lista desde atrás
print(mi_lista[-3]) #Pepe

#Para acceder a un grupo de la lista
print(mi_lista[0:3]) #María, Pepe, Marta

print(mi_lista[:3]) #Lo mismo

print(mi_lista[2:]) #Marta, Antonio

#Agregar elementos al final de la lista
mi_lista.append("Sandra")

#Agregar elementos en una posición en concreto
mi_lista.insert(2, "Sandra")

#Agregar varios elementos a la lista
mi_lista.extend(["Ana", "Lucía"])

#Para saber en qué posición se encuentra algún elemento
print(mi_lista.index("María"))

#Si un elemento se encuentra o no en la lista
print("Pepe" in mi_lista)

#Eliminar elementos
mi_lista.remove(5)

#Eliminar último elemento de una lista
mi_lista.pop()

#Sumar una lista a otra
mi_lista2 = ["Juan", "Mecánico"]

mi_lista3 = mi_lista + mi_lista2

print(mi_lista3[:])

#Repetir listas
mi_lista4 = ["Elegante", "Keloke"] * 3

print(mi_lista4[:])


#LIST COMPREHENSION

mi_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(mi_original_list)

#Generando listas con un mecanismo rápido, y se modifica en el momento en el que se va creando
my_range = range(8)
print(list(my_range))

my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)