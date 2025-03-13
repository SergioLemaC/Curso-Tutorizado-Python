import math

def divide(num1, num2):
    try:
        return num1 / num2

    except ZeroDivisionError:
        print("No se puede dividir entre 0")

        return "Operación errónea"
    
print(divide(8, 2))

def divide2():
    try:
        op1 = (float(input("Introduce el primer número: ")))

        op2 = (float(input("Introduce el segundo número: ")))

        print("La división es: " + str(op1 / op2))
    
    except ValueError:
        print("El valor introducido es erróneo")
    
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    finally:
        print("Cálculo finalizado")
    
def evalua_edad(edad):
    if (edad < 0):
        raise TypeError("No se permiten edades negativas")

    if (edad < 20):
        return "Eres muy joven"
    
    elif(edad < 40):
        return "Eres joven"
    
    elif(edad < 65):
        return "Eres maduro"
    
    elif(edad < 100):
        return "Cuídate..."
    
print(evalua_edad(18))

def calcula_raiz(num1):
    if(num1 < 0):
        raise ValueError("El número no puede ser negativo")
    
    else:
        return math.sqrt(num1)

op1 = int(input("Introduce un número: "))

try:    
    print(calcula_raiz(op1))

except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")