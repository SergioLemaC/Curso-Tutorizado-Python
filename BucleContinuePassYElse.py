#Continue: salta a la siguiente interacción de bucle
for letra in "Python":

    if (letra == "h"):
        continue #Ignorar el resto del bucle y pasar a la siguiente iteración

    print("Viendo la letra: " + letra)

#Pass: Devuelve un null, es como si el bucle no se ejecutase
#while True:
    #pass

#Else: Por si al recorrer el bucle no sucede nada
email = input("Introduce tu email, por favor")

for i in email:

    if(i == "@"):
        arroba = True
        break;

else:
    arroba = False

print(arroba)