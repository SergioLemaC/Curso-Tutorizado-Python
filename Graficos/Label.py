from tkinter import *

root = Tk()

mi_frame = Frame(root, width=500, height=400)

mi_frame.pack()

#mi_label = Label(mi_frame, text="Hola alumnos de Python")

#Nos permite ubicar ese texto en cualquier lugar usando coordenadas
#mi_label.place(x=100, y=200)

#Queremos usar imágenes
mi_imagen = PhotoImage(file="mouse.gif")
#Label(mi_frame, image=mi_imagen).place(x=100, y=200)

#Abreviando y usando más opciones
Label(mi_frame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)


root.mainloop()