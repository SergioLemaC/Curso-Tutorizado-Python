class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

#Esta clase de polimorfismo la veo para la necesidad de usar funciones sobreescritas
#sin necesidad de estar instanciando tantos objetos de cada tipo, sino que con un solo objeto, ya que Python 
#es dinámico, lo puede tomar según el tipo de objeto que se instancie

def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

mi_vehiculo = Camion()

desplazamiento_vehiculo(mi_vehiculo)