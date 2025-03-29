from datetime import datetime, timedelta

#Para idiomas de fechas
import locale

#Obtener fecha y hora actual
now = datetime.now()

#Crear fecha y hora específica
specific_date = datetime(2025, 1, 12)

#Formatear fechas strftime()
format_date = now.strftime("%d/%m/%Y") #También se puede agregar la hora (%H:%M:%S)

#Operaciones con fechas (sumar, restar días-minutos-horas-meses)
yesterday = datetime.now() - timedelta(days=1)

tomorrow = datetime.now() + timedelta(days=1)

one_hour_after = datetime.now() + timedelta(hours=1)

#Obtener componentes individuales de una fecha
year = now.year

month = now.month

#Calcular la diferencias entre dos fechas
date1 = datetime.now()

date2 = datetime(2025, 2, 12, 15, 30, 0)

difference = date2 - date1

#Fecha en otro idioma
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

format_date = now.strftime("%A/%B/%Y %H:%M:%S")

print(format_date)