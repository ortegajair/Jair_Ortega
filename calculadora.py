import tkinter as tk
from tkinter import messagebox

def calcular():
    # Obtener y limpiar la letra del menú
    operacion = entry_operacion.get().strip().upper()
    
    # Validar que los campos de números no estén vacíos
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")
        return

    # Realizar la operación según la primera letra
    if operacion == 'S':
        resultado = num1 + num2
        simbolo = "+"
    elif operacion == 'R':
        resultado = num1 - num2
        simbolo = "-"
    elif operacion == 'M':
        resultado = num1 * num2
        simbolo = "*"
    elif operacion == 'D':
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
            return
        resultado = num1 / num2
        simbolo = "/"
    else:
        messagebox.showerror("Error", "Opción no válida. Usa S, R, M o D.")
        return

    # Mostrar el resultado en la etiqueta
    lbl_resultado.config(text=f"Resultado: {num1} {simbolo} {num2} = {resultado}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Mini Calculadora")
ventana.geometry("320x280")
ventana.resizable(False, False)

# Menú de instrucciones
menu_texto = "Selecciona la operación:\n[S] Sumar | [R] Restar\n[M] Multiplicar | [D] Dividir"
lbl_menu = tk.Label(ventana, text=menu_texto, justify="center", font=("Arial", 10, "bold"))
lbl_menu.pack(pady=10)

# Campo para elegir la operación
frame_op = tk.Frame(ventana)
frame_op.pack(pady=5)
tk.Label(frame_op, text="Operación (S/R/M/D): ").pack(side=tk.LEFT)
entry_operacion = tk.Entry(frame_op, width=5, justify="center")
entry_operacion.pack(side=tk.LEFT)

# Campo Número 1
frame_n1 = tk.Frame(ventana)
frame_n1.pack(pady=5)
tk.Label(frame_n1, text="Número 1: ").pack(side=tk.LEFT)
entry_num1 = tk.Entry(frame_n1, width=15)
entry_num1.pack(side=tk.LEFT)

# Campo Número 2
frame_n2 = tk.Frame(ventana)
frame_n2.pack(pady=5)
tk.Label(frame_n2, text="Número 2: ").pack(side=tk.LEFT)
entry_num2 = tk.Entry(frame_n2, width=15)
entry_num2.pack(side=tk.LEFT)

# Botón de cálculo
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_calcular.pack(pady=15)

# Etiqueta para mostrar el resultado
lbl_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 11, "bold"))
lbl_resultado.pack()

# Ejecutar la aplicación
ventana.mainloop()