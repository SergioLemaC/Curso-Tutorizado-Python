"""Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc

-Búsqueda avanzada: Encontrar patrones específicos en texto grande de forma rápida y precisa

-Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc sean correctos

-Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

#Importar el módulo de expresiones regulares "re"
import re

#Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"

#El texto donde queremos buscar
text = "Hola mundo"

#Usar la función de búsqueda de "re"
result = re.search(pattern, text)

if (result):
    print("He encontrado el patrón en el texto")
else:
    print("No lo he encontrado")

# .group() devuelve la cadena que coincide con el pattern
print(result.group())

# .start() devuelve la posición inicial de la coincidencia
print(result.start())

# .end() devuelve la posición final de la coincidencia
print(result.end())

#Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias
text = "Me gusta Python. Python es lo máximo. Aunque " \
"Python no es tan difícil, ojo con Python"

pattern = "Python"

matches = re.findall(pattern, text)

print(matches)

# .finditer() devuelve un iterador que contiene todos los resultados de la búsqueda
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

# re.IGNORECASE ignora las mayúsculas y minúsculas
found_python = re.findall(pattern, text, re.IGNORECASE)

#text = "Me gusta Python. PYTHON es lo máximo. Aunque " \
#"pYTHON no es tan difícil, ojo con Python"

if found_python: print(found_python)

# .sub() reemplaza todas las coincidencias de un patrón en un texto
text = "Hola mundo, Hola de nuevo."

pattern = "Hola"

replacement = "Adiós"

new_text = re.sub(pattern, replacement, text)

print(new_text)

#METACARACTERES - METACHARS

#Los metacaracteres son símbolos especiales con significados específicos en las 
#expresiones regulares

#El punto (.)
#Coincidir con cualquier caracter excepto una nueva línea o salto de línea
text = "Hola mundo, H0la de nuevo, H0la otra vez"

pattern = "H.la"

found = re.findall(pattern, text)

if(found):
    print(found)
else:
    print("No se ha encontrado el patrón")

#Barra invertida para anular el significado especial de un símbolo
text = "Mi casa es blanca. Y el coche es negro."

pattern = r"\."

# \d: coincide con cualquier dígito (0-9) uno solo
text = "El número de teléfono es 123456789"

#found = re.findall(r"\d", text) -> para buscar un dígito

found = re.findall(r"\d{9}", text)

print(found)

#Ejercicio
text = "Mi número de teléfono es +34 688999999 apúntalo vale¿?"

pattern = r"\+34 \d{9}"

found = re.search(pattern, text)

if found: print(f"Encontré el número de teléfono {found.group()}")

# \w: coincide con cualquier caracter alfanumérico (a-z, A-Z, 0-9, _)
text = "el_rubius_69"

pattern = r"\w"

# \s: coincide con cualquier espacio, tabulación, salto de línea
text = "Hola mundo\nCómo estás¿?\t"

pattern = r"\s"

# ^: coincide con el principio de una cadena, para detectar si un string empieza de una forma
username = "%423_name"

pattern = r"^\w" #Validar nombre de usuario por ejemplo

valid = re.search(pattern, username)

if (valid): print("El nombre de usuario es válido")
else: print("El nombre de usuario no es válido")

#Valida número de teléfono
phone = "+34 688999999"

pattern = r"^\+\d{1,3} "

valid = re.search(pattern, phone)

# $: coincide con el final de una cadena
text = "Hola mundo"

pattern = r"mundo$"

#Ejercicio

#Valida un correo que sea de Gmail
text = "miduga@gmail.com"

pattern = r"@gmail.com$"

# \b: coincide con el principio o final de una palabra, osea una palabra exacta del texto
text = "casa casada casado"

pattern = r"\bcasa\b"

# |: coincide con una opción u otra, como si fuera un or
fruits = "plátano, manzana, aguacate, palta, pera"

pattern = r"palta|aguacate"

# CUANTIFICADORES - QUANTIFIERS

#Los cuantificadores se usan para especificar cuántas ocurrencias de un caracter o grupo de caracteres 
#se deben encontrar en una cadena

# *: pueden aparecer 0 o más veces
text = "aaaba"

pattern = "a*"

# +: pueden aparecer una o más veces
text = "ddd aaa ccc bb"

pattern = "a+"

# ?: puede aparecer cero o una vez
text = "aaaba"

pattern = "a?b" #La a puede aparecer antes que la b

# {n}: exactamente n veces
text = "aaaaaa"

pattern = "a{3}" #Que aparezca 3 veces

# {n, m}: de n a m veces
text = "u uu uuu u"

pattern = "u{2,3}"

matches = re.findall(pattern, text)

print(matches)

# [: coincide con cualquier caracter dentro de los corchetes
username = "rub.ius_69+"

pattern = r"^[\w._%+-]+$"

# [^]: coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"

pattern = r"[^aeiou]"