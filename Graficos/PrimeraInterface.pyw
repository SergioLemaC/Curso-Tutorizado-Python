from tkinter import *

#Crear la primera ventana (raíz)
raiz = Tk()

#Título de una ventana
raiz.title("Ventana de pruebas")

#Que la ventana sea resizable o no
#raiz.resizable(True, False)

#Añadir imagen al ícono
#raiz.iconbitmap("gato.ico")

#Cambiar tamaño de la ventana
#raiz.geometry("650x350")

#Color de fondo
raiz.config(bg="blue")

#Para evitar que abra la consola al ejecutar, se le cambia la extensión al archivo py a pyw

#Creando un frame, hay que empaquetarlo y meterlo dentro de la raíz
mi_frame = Frame()

mi_frame.pack() #side="right" para anclar el frame a la derecha, "bottom" se ancla abajo; todo esto al redimensionar la raíz
#"anchor" para usar puntos cardinales; anchor="n" north
#"fill" para rellenar; fill="y" (x,y,both,none)

mi_frame.config(bg="red")

mi_frame.config(width="650", height="350")

#Aplicar un tipo de borde al frame
mi_frame.config(bd=35)
mi_frame.config(relief="groove")

#Cambiar el cursor cuando pase sobre el frame
mi_frame.config(cursor="pirate") #"pirate" le da forma de calavera

raiz.mainloop()