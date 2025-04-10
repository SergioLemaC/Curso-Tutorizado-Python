import pickle

class Persona():

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

        print("Se ha creado una persona nueva con el nombre de:", self.nombre)

    def __str__(self):
        return f"{self.nombre} {self.genero} {self.edad}"
        #return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
class ListaPersonas():

    personas = []

    def __init__(self):
        lista_de_personas = open("fichero_externo", "ab+")
        lista_de_personas.seek(0)

        try:
            self.personas = pickle.load(lista_de_personas)
            print(" Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            lista_de_personas.close()
            del(lista_de_personas)

    def agregar_personas(self, p):
        self.personas.append(p)
        self.guardar_personas_en_fichero_externo()

    def mostrar_personas(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)
    
    def guardar_personas_en_fichero_externo(self):
        lista_de_personas = open("fichero_externo", "wb")
        pickle.dump(self.personas, lista_de_personas)
        lista_de_personas.close()
        del(lista_de_personas)

mi_lista = ListaPersonas()

p = Persona("Sandra", "Femenino", 29)
mi_lista.agregar_personas(p)

p = Persona("Antonio", "Masculino", 39)
mi_lista.agregar_personas(p)

p = Persona("Ana", "Femenino", 19)
mi_lista.agregar_personas(p)

mi_lista.mostrar_personas()