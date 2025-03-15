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
class VElectricos():

    def __init__(self):
        self.autonomia = 100

    def cargar_energia(self):
        self.cargando = True

#Crear instancias para comprobar que la clase Moto hereda de Vehiculos
mi_moto = Moto("Honda", "CBR")

mi_moto.caballito()

mi_moto.estado()

#Furgoneta
mi_furgoneta = Furgoneta("Renault", "Kangoo")

mi_furgoneta.arrancar()

mi_furgoneta.estado()

print(mi_furgoneta.carga(True))

#Clase BicicletaElectrica para herencia múltiple
class BicicletaElectrica(VElectricos, Vehiculos):
    pass

#Al instanciar esta clase, le da prioridad al constructor de la primera clase que hereda (Vehiculos)
mi_bici = BicicletaElectrica()