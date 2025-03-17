import pickle

#Creamos la lista, el archivo y lo volcamos a binario
lista_nombres = ["Pedro", "Ana", "María", "Isabel"]

#"wb" escritura binaria
fichero_binario = open("lista_nombres", "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario)

#Recuperamos el archivo y leerlo para recuperar la información
fichero = open("lista_nombres", "rb") #"rb" para leer binarios

lista = pickle.load(fichero)

print(lista)