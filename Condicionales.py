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

print("Programa de becas año 2017")

distancia_escuela = int(input("Introduce la distancia a la escuela en km "))

print(distancia_escuela)

numero_hermanos = int(input("Introduce el número de hermanos en el centro "))

print(numero_hermanos)

salario_familiar = int(input("Introduce salario anual bruto "))

print(salario_familiar)

if(distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000):
    print("Tienes derecho a beca")

else:
    print("No tienes derecho a beca")


#Escoger asignatura optativa

print("Asignaturas optativas")

print("Informática gráfica - Pruebas de Software - Usabilidad y accesibilidad")

opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower()

if(asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad")):
    print("Asignatura elegida " + asignatura)

else:
    print("La asignatura escogida no está contemplada")