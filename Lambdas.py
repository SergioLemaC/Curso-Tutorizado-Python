# Se entiende como una función implícita, no tiene nombre

#Podemos almacenar funciones lambda, y esta variable se comporta como función
sum_two_values = lambda first_value, second_value: print(first_value + second_value)

sum_two_values(2, 4)

#Una función que dentro tiene una lambda
def sum_values(firs_value):
    return sum_two_values

def sum_three_values(value):
    return lambda first_value, second_value : first_value + second_value + value

#Al parecer primero recibe el valor de la propia función y aparte los argumentos que necesita la lambda
print(sum_three_values(5)(2, 4))