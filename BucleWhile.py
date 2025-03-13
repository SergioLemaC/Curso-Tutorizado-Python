import math

i = 1

while (i <= 10):
    print("Ejecución " + str(i))
    i = i + 1

edad = int(input("Introduce la edad por favor: "))

while (edad < 5 or edad > 100):
    print("Haz introducido una edad incorrecta. Vuelve a intentarlo")
    edad = int(input("Introduce la edad por favor: "))

print("Gracias por colaborar. Puedes pasar")

print("Edad del aspirante " + str(edad))

#Averiguar raíz cuadrada

print("Programa de cálculo de raíz cuadrada")

numero = int(input("Introduce un número por favor: "))

intentos = 0

while(numero < 0):
    print("No se puede hallar la raíz de un número negativo")

    if(intentos == 2):
        print("Haz consumido demasiados intentos. El programa ha finalizado")
        break;

    numero = int(input("Introduce un número por favor: "))

    if(numero < 0):
        intentos = intentos + 1

if(intentos < 2):
    solucion = math.sqrt(numero)
    print("La raíz cuadrada de  " + str(numero) + " es " + str(solucion))

print("Terminó la ejecución")