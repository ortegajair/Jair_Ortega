def guardar_reporte(nombre_completo, puntos, estado, mensaje):
    # Genera un archivo individual basado en el nombre del estudiante
    nombre_archivo = (
        f"reporte_{nombre_completo.lower().replace(' ', '_')}.txt"
    )

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("==================================================\n")
        archivo.write("           REPORTE ESCOLAR DE CONDUCTA            \n")
        archivo.write("==================================================\n")
        archivo.write(f"Fecha:{fecha}\n")
        archivo.write(f"Estudiante: {nombre_completo.upper()}\n")
        archivo.write(f"Reglas cumplidas: {puntos} / 5\n")
        archivo.write(f"Estado: [{estado}]\n")
        archivo.write(f"Diagnóstico: {mensaje}\n")
        archivo.write("==================================================\n")

    print(f"\n[✓] El reporte ha sido guardado exitosamente en '{nombre_archivo}'.")


# --- ENCABEZADO ---
print("==================================================")
print("     SISTEMA DE EVALUACIÓN DE REGLAS DE CLASE     ")
print("==================================================\n")

# Entrada del estudiante
nombre = input("Ingrese el nombre del estudiante: ").strip()
apellido = input("Ingrese el apellido del estudiante: ").strip()
nombre_completo = f"{nombre} {apellido}"
fecha=input("Ingresa la fecha del reporte:")

print(f"\nVerificando reglamento para: {nombre_completo.upper()}")
print("Responde con 'si' o 'no' a cada una de las siguientes preguntas:\n")

puntos = 0

# --- REGLA 1 ---
r1 = input("1. ¿Llegó dentro de los 5 minutos de tolerancia? (si/no): ").lower()
if r1 == "si":
    puntos += 1

# --- REGLA 2 ---
r2 = input("2. ¿Evitó comer dentro del aula durante la clase? (si/no): ").lower()
if r2 == "si":
    puntos += 1

# --- REGLA 3 ---
r3 = input("3. ¿Trae el uniforme completo y bien portado? (si/no): ").lower()
if r3 == "si":
    puntos += 1

# --- REGLA 4 ---
r4 = input(
    "4. ¿Mantuvo el respeto hacia el profesor y sus compañeros? (si/no): "
).lower()
if r4 == "si":
    puntos += 1

# --- REGLA 5 ---
r5 = input(
    "5. ¿Mantuvo su celular guardado durante la clase? (si/no): "
).lower()
if r5 == "si":
    puntos += 1


# --- EVALUACIÓN CON IF / ELIF / ELSE ---
print("\n" + "=" * 50)
print(f"             REPORTE FINAL: {nombre_completo.upper()}")
print("=" * 50)
print(f"Reglas cumplidas: {puntos} / 5\n")

if puntos > 4:  # Es decir, 5 puntos
    estado = "EXCELENTE"
    mensaje = "Cumple con todas las reglas del aula. ¡Felicitaciones!"
elif puntos == 4:
    estado = "ACEPTABLE"
    mensaje = "Cumple casi todas las reglas. Hay un pequeño aspecto por mejorar."
else:  # Menos de 4 puntos
    estado = "INFRACCIÓN"
    mensaje = "Incumple las reglas del aula. Se notificará a inspección/tutoría."

print(f"ESTADO: [{estado}]")
print(f"DIAGNÓSTICO: {mensaje}")
print("=" * 50)

# Llamada a la función para guardar el archivo .txt
guardar_reporte(nombre_completo, puntos, estado, mensaje)