import tkinter as tk

ventana = tk.Tk()
ventana.title("Hola Mundo")
ventana.geometry("500x200")

etiqueta = tk.Label(ventana, text="¡Hola desde tkinter!")
etiqueta.pack()

boton = tk.Button(ventana, text="Cerrar", command=ventana.quit)
boton.pack()

ventana.mainloop()
