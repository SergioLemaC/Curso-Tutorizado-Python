#Para la herencia usamos la función "super()" para llamar a los constructores de la clase padre y también a las funciones
class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre:", self.nombre, ", Edad:", self.edad, ", Residencia:", self.lugar_residencia)

class Empleado(Persona):

    #Con el constructor recibimos los parámetros para alimentar la clase que hereda de la superclase
    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
        #Llamando al constructor de la clase padre "Persona"
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antigüedad = antigüedad

    def descripcion(self):
        #Llamamos a la función de la clase padre "Persona" y sobreescribimos la misma
        super().descripcion()
        print("Salario:", self.salario, "Antigüedad:", self.antigüedad, "años")

#Instanciamos la clase Empleado que hereda de Persona y le pasamos los argumentos para que las clases se complementen entre sí
manuel = Empleado(1500, 15, "Manuel", 55, "Colombia")

manuel.descripcion()

#Para saber si un objeto es una instancia de una clase
print(isinstance(manuel, Empleado))
print(isinstance(manuel, Persona))