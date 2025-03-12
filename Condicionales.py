print("Programa de evaluación de notas de alumnos")

nota_alumno = int(input("Introduce la nota del alumno: "))

def evaluacion(nota):

    valoracion = "Aprobado"

    if (nota < 5):
        valoracion = "Suspenso"
    
    return valoracion

print(evaluacion(nota_alumno))


print("Verificación de acceso")

edad_usuario = int(input("Introduce tu edad, por favor "))

if(edad_usuario < 18):
    print("No puedes pasar")

elif(edad_usuario > 100):
    print("Edad incorrecta")

else:
    print("Puedes pasar")

print("El programa ha finalizado")

#Otra clase de evaluar condiciones
edad = -7

if (0<edad<100):
    print("Edad es correcta")

else:
    print("Edad incorrecta")