mensaje = "Hola Python"

print(mensaje); print("Keloke")

#Comentarios

miNombre = "Mi nombre es Juan"

miNombre = "Mi nombre es \
    Juan" #Salto de línea \

#Operadores 

#Aritméticos; Suma "+", Resta "-", Multiplicación "*", División "/", Módulo "%", Exponente "**", División entera "//"

#Comparación; Igual qué "==", Diferente de "!=", Mayor qué ">", Menor qué "<", Mayor o igual qué ">=", Menor o igual qué "<="

#Lógicos; AND, OR, NOT

#Asignación; Igual "=", Incremento "=+", Decremento "-=", (*=), (/=), (%=), (**=), (//=)

#Especiales; IS, IS NOT, IN, NOT IN

num1 = 5
num2 = 7

if (num1 > num2):
    print("El número "); print(num1); print(" es mayor que el número "); print(num2)
else:
    print("El número "); print(num2); print(" es mayor que el número "); print(num1)



#Consultar el tipo de dato con la función type()
print(type("Hola mundo")) #Tipo str
print(type(5)) #Tipo int
print(type(1.5)) #Tipo float
print(type(True)) #Tipo bool
print(type(3 + 1j)) #Tipo complex

#Variables
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

print(my_string_variable, my_int_variable, my_bool_variable)