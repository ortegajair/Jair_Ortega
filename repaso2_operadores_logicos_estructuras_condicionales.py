edad=18
calificacion=8.5
tiene_cedula=True


if edad>=18 and tiene_cedula and calificacion >=8.0:
    print("Acceso contenido al programa de honor.")
elif edad>=18 and tiene_cedula and calificacion <8.0:
    print("Acceso regular.")
else:
    print("Acceso denegado.")