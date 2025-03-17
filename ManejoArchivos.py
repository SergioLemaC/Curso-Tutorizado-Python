from io import open

#Para crear un archivo externo donde almacenaremos algo
#archivo_texto = open("archivo.txt", "w")

#frase = "Estupendo día para estudiar Python"

#archivo_texto.write(frase)

#archivo_texto.close()

#Abrir el archivo en modo lectura
archivo_texto = open("archivo.txt", "r+") #"r+" usando este parámetro indicamos que es lectura y escritura

#texto = archivo_texto.read()

#archivo_texto.close()

#print(texto)

#Almacena la información en una lista
#lineas_texto = archivo_texto.readlines()

#archivo_texto.close()

#print(lineas_texto)

#Editar el archivo
#archivo_texto = open("archivo.txt", "a")

#archivo_texto.write("\n siempre es una buena ocasión para estudiar Python")

#archivo_texto.close()

#Función seek() para usar el cursor o índice donde se sitúa en el contenido del archivo
#print(archivo_texto.read())

#archivo_texto.seek(11)

#print(archivo_texto.read())

#archivo_texto.seek(0)

#print(archivo_texto.read())

#Modificar archivo usando listas
lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta línea ha sido incluída desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()