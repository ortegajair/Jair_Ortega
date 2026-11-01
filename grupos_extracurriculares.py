grupo_futbol = {"Ana", "Carlos", "Luis", "Maria", "Pedro", "Sofia"}
grupo_programacion = {"Carlos", "Maria", "Diego", "Sofia", "Andres"}


total_estudiantes = list(grupo_futbol | grupo_programacion)

solo_futbol = list(grupo_futbol - grupo_programacion)
solo_programacion = list(grupo_programacion - grupo_futbol)
ambos_grupos = list(grupo_futbol & grupo_programacion)

print(f"Estudiantes que conforman los grupos: {total_estudiantes} \n")
print(f"Estudiantes solo en futbol: {solo_futbol}\n")
print(f"Estudiantes solo en programacion: {solo_programacion}\n")
print(f"Estudiantes en ambos grupos: {ambos_grupos}\n")