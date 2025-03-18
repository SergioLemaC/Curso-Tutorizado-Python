#Ventajas f-strings vs .format()

nombre = "Juan"
edad = 25

#f-strings
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

#.format()
print("Hola, mi nombre es {} y tengo {} años.".format(nombre, edad))

x, y = 10, 20

print(f"La suma de {x} y {y} es {x + y}.")

print("La suma de {} y {} es {}.".format(x, y, x + y))

#Sirve para hacer cálculos de tiempos de ejecución de programas
import timeit

#f-strings
calculo_f_string = timeit.timeit('f"Hola {nombre} tienes {edad} años."', globals=globals(), number=1000000)

#Usando .format()
calculo_format = timeit.timeit('"Hola {} tienes {} años.".format(nombre, edad)', globals=globals(), number=1000000)

print(f"Tiempo usando f-strings: {calculo_f_string} segundos")
print(f"Tiempo usando .format(): {calculo_format} segundos")

pi = 3.14159
print(f"El valor de pi es {pi:.2f}")

print("El valor de pi es {:.2f}".format(pi))