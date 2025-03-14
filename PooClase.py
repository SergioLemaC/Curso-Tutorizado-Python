class Coche():

    #Método constructor
    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4 #Encapsulamiento con __
        self.__en_marcha = False

    #Función normalele de clase, self (this en Java)
    def arrancar(self, arrancamos):
        self.__en_marcha = arrancamos

        if(self.__en_marcha):
            chequeo = self.__chequeo_interno()

        if(self.__en_marcha and chequeo):
            return "El coche está en marcha"
        elif(self.__en_marcha and chequeo == False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__ancho_chasis, "y un largo de", self.__largo_chasis)

    #Encapsulamiento de la función para que no sea accesible desde fuera de la clase
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "Ok"
        self.aceite = "Mal"
        self.puertas = "Cerradas"

        if(self.gasolina == "Ok" and self.aceite == "Ok" and self.puertas == "Cerradas"):
            return True
        else:
            return False

#Instanciar la clase (crear objeto)
mi_coche = Coche()

#Getter en Java, para ver las propiedades del objeto, omitimos los paréntesis porque es una propiedad, no una función
#print(mi_coche.largo_chasis)

print(mi_coche.arrancar(True))

mi_coche.estado()

print("---------A continuación creamos el segundo objeto----------")

mi_coche2 = Coche()

print(mi_coche2.arrancar(False))

mi_coche2.estado()