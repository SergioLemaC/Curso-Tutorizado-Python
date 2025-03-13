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