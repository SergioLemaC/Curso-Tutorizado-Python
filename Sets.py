# Es como una lista que no es ordenada, y que no almacena datos repetidos

#Se puede definir así
my_set = set()

#Y así, aunque así se interpreta como diccionario
my_other_set = {}

#Pero al llenarlo es un set
my_other_set = {"Brais", "Moure", 35}

my_other_set.add("MoureDev")

print(my_other_set)

#Comprobando si existe un elemento en el set
print("Moure" in my_other_set) 

#Eliminar elementos del set
my_other_set.remove("Moure")

#Vaciar el set
my_other_set.clear()

#Ojo que con esto eliminamos el set pero de la memoria
del my_other_set

#Para convertir un set en una lista aunque no es recomendable
my_set = {"Brais", "Moure", 35}

my_list = list(my_set)

#Para unir sets
my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)

print(my_new_set)