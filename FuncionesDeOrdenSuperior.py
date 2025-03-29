# Funciones que usan funciones dentro

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

#/def sum_two_values_and_one(first_value, second_value):
    #return sum_one(first_value + second_value)

#print(sum_two_values_and_one(5, 2)) #8

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))

print(sum_two_values_and_add_value(5, 2, sum_five))


# Closures
# Es el concepto de función que define una función y retorna una función
print("CLOSURES")

def sum_ten(original_value):
    print(original_value)
    def add(value):
        return value + 10 + original_value
    
    return add
    
add_closure = sum_ten(5)
print(add_closure(5)) #20

#Podemos llamarlo como una lambda
print(sum_ten(5)(1)) #16


# Funciones de orden superior

# Map
numbers = [2, 5, 10, 21, 3, 30]

def multiply_two(number):
    return number * 2

# map itera cada uno de los elementos que tenemos en nuestro elemento iterable (numbers) y sobre
# cada valor ha ejecutado la función (multiply_two)
print(list(map(multiply_two, numbers)))

print(list(map(lambda number: number * 2, numbers)))

# Filter
def filter_greater_than_ten(number):
    if (number > 10):
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))

print(list(filter(lambda number: number > 10, numbers)))

# Reduce
# opera con un valor más el acumulado
from functools import reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))