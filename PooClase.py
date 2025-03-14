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
            return "El coche está en marcha"
        else:
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__ancho_chasis, "y un largo de", self.__largo_chasis)

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