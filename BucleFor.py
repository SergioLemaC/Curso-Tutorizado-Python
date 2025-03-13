for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
    print(i)

contador = 0

mi_email = input("Introduce tu dirección de email: ")

for i in mi_email:
    
    if(i == "@" or i == "."):
        contador = contador + 1

if(contador == 2):
    print("El email es correcto")

else:
    print("El email no es correcto")

for i in range(5):
    print("Hola")
    print(f"Valor de la variable {i}")

#for i in range(5, 10): Debe contar desde el 5 hasta el 9
#for i in range(5, 50, 3): Debe contar desde el 5 hasta el 49 de 3 en 3

valido = False

email = input("Introduce tu email: ")

for i in range(len(email)):

    if(email[i] == "@"):
        valido = True

if (valido):
    print("Email correcto")

else:
    print("Email incorrecto")