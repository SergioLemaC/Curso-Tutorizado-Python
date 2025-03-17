import pickle

class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.en_marcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
    
    def estado(self):
        print("Marca:", self.marca, "\n"
              "Modelo:", self.modelo, "\n"
              "En marcha:", self.en_marcha, "\n"
              "Acelerando:", self.acelera, "\n"
              "Frenando:", self.frena)
        
coche1 = Vehiculo("Mazda", "MX5")
coche2 = Vehiculo("Seat", "Leon")
coche3 = Vehiculo("Renault", "Megane")

#Para no serializar de uno en uno, los guardamos en una colección y serializamos esa colección
coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb")

#Volcado de información
pickle.dump(coches, fichero)

fichero.close()

del(fichero)

#Ahora rescatamos la información de ese fichero
fichero_apertura = open("losCoches", "rb")

misCoches = pickle.load(fichero_apertura)

fichero_apertura.close()

for c in misCoches:
    print(c.estado())