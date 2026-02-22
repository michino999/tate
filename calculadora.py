import tkinter as tk
import math

# ------------------ VENTANA ------------------
ventana = tk.Tk()
ventana.title("Calculadora Pro")
ventana.geometry("320x450")
ventana.configure(bg="#1e1e1e")
ventana.resizable(False, False)

# ------------------ PANTALLA ------------------
entrada = tk.Entry(
    ventana,
    font=("Segoe UI", 24),
    bg="#252526",
    fg="white",
    bd=0,
    justify="right"
)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew", ipady=10)

# ------------------ FUNCIONES ------------------

def click(valor):
    entrada.insert(tk.END, valor)

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        expresion = entrada.get()
        expresion = expresion.replace('%', '/100')
        expresion = expresion.replace('^', '**')

        resultado = eval(expresion)

        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)

    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def raiz():
    try:
        numero = float(entrada.get())
        resultado = math.sqrt(numero)

        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# ------------------ ESTILO BOTONES ------------------

def crear_boton(texto, fila, columna, comando, color="#3a3a3a"):
    boton = tk.Button(
        ventana,
        text=texto,
        command=comando,
        font=("Segoe UI", 14, "bold"),
        bg=color,
        fg="white",
        bd=0,
        activebackground="#505050",
        activeforeground="white",
        cursor="hand2"
    )
    boton.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5, ipadx=5, ipady=15)

# ------------------ BOTONES ------------------

crear_boton("C", 1, 0, limpiar, "#d9534f")
crear_boton("√", 1, 1, raiz, "#5bc0de")
crear_boton("^", 1, 2, lambda: click("^"), "#5bc0de")
crear_boton("/", 1, 3, lambda: click("/"), "#f0ad4e")

crear_boton("7", 2, 0, lambda: click("7"))
crear_boton("8", 2, 1, lambda: click("8"))
crear_boton("9", 2, 2, lambda: click("9"))
crear_boton("*", 2, 3, lambda: click("*"), "#f0ad4e")

crear_boton("4", 3, 0, lambda: click("4"))
crear_boton("5", 3, 1, lambda: click("5"))
crear_boton("6", 3, 2, lambda: click("6"))
crear_boton("-", 3, 3, lambda: click("-"), "#f0ad4e")

crear_boton("1", 4, 0, lambda: click("1"))
crear_boton("2", 4, 1, lambda: click("2"))
crear_boton("3", 4, 2, lambda: click("3"))
crear_boton("+", 4, 3, lambda: click("+"), "#f0ad4e")

crear_boton("0", 5, 0, lambda: click("0"))
crear_boton(".", 5, 1, lambda: click("."))
crear_boton("=", 5, 2, calcular, "#5cb85c")

# ------------------ AJUSTE DE GRID ------------------

for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)

for j in range(4):
    ventana.grid_columnconfigure(j, weight=1)

ventana.mainloop()

