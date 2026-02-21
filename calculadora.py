import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora Pro 😼")
ventana.geometry("300x400")
ventana.resizable(False, False)

# Pantalla
entrada = tk.Entry(ventana, font=("Arial", 20), borderwidth=5, relief="ridge")
entrada.pack(pady=10, padx=10, fill="both")

# Función para agregar números
def click(boton):
    entrada.insert(tk.END, boton)

# Función para calcular
def calcular():
    try:
        expresion = entrada.get ()
         # Convertir % en /100
        expresion = expresion.replace('%', '/100')
        
        resultado = eval(expresion)
        
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Función para limpiar
def limpiar():
    entrada.delete(0, tk.END)

# Botones
botones = [
            '7','8','9','/',
           '4','5','6','*',
           '1','2','3','-',
           '0','.','%','+',
           '=']

frame = tk.Frame(ventana)
frame.pack()

fila = 0
columna = 0

for boton in botones:
    if boton == "=":
        tk.Button(frame, text=boton, width=5, height=2,
                  command=calcular).grid(row=fila, column=columna)
    else:
        tk.Button(frame, text=boton, width=5, height=2,
                  command=lambda b=boton: click(b)).grid(row=fila, column=columna)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botón limpiar
tk.Button(ventana, text="C", width=20, height=2,
          command=limpiar).pack(pady=5)

ventana.mainloop()