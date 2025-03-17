#En este módulo se pretende incluir todas las clases que hemos creado de Motos etcetc
class Vehiculos():

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

#Clase Furgoneta
class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar

        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

#Clase Moto heredando propiedades y funciones de la clase Vehiculos
class Moto(Vehiculos):
    
    enllantar = ""

    def caballito(self):
        self.enllantar = "Voy haciendo el caballito"

    #Sobreescribiendo la función de la clase Vehiculos en esta clase
    def estado(self):
        print("Marca:", self.marca, "\n"
              "Modelo:", self.modelo, "\n"
              "En marcha:", self.en_marcha, "\n"
              "Acelerando:", self.acelera, "\n"
              "Frenando:", self.frena, "\n",
              self.enllantar)

#Clase VElectricos
class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargar_energia(self):
        self.cargando = True