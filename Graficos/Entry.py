from tkinter import *

raiz = Tk()

mi_frame = Frame(raiz, width=1200, height=600)
mi_frame.pack()

mi_nombre = StringVar()

#creando cuadro de texto
cuadro_texto = Entry(mi_frame, textvariable=mi_nombre)
#Para ubicar el elemento podemos usar "grid()" para hacer el frame como cuadrilla y organizar los elementos
cuadro_texto.grid(row=0, column=1)

nombre_label = Label(mi_frame, text="Nombre:")
nombre_label.grid(row=0, column=0)

cuadro_password = Entry(mi_frame)
cuadro_password.grid(row=1, column=1, padx=10, pady=10)

#Cuadros de contraseña
password_label = Label(mi_frame, text="Password:")
#"sticky" para colocar adecuadamente los elementos, se usa norte, sur etc (w, n, s, e, ne, se, sw, nw)
password_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
cuadro_password.config(show="*") #Para que muestre estos caracteres

comentarios_label = Label(mi_frame, text="Comentarios:")
comentarios_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

#Introducir texto largo
cuadro_comentarios = Text(mi_frame, width=16, height=5)
cuadro_comentarios.grid(row=2, column=1, padx=10, pady=10)
#Agregar scroll
scroll_vertical = Scrollbar(mi_frame, command=cuadro_comentarios.yview)
scroll_vertical.grid(row=2, column=2, sticky="nsew")
cuadro_comentarios.config(yscrollcommand=scroll_vertical.set)

#Agregar botón y "codigo_boton" que es la función que hace el botón
def codigo_boton():
    mi_nombre.set("Juan")

boton_envio = Button(raiz, text="Enviar", command=codigo_boton)
boton_envio.pack()

raiz.mainloop()