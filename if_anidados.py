
email = input("Ingresa tu correo: ")
contraseña = input("Ingresa tu contraseña: ")

if email == "jairortega232454":
    if contraseña == "03072009":
        codigo = input("Ingresa el código de área: ")

        if codigo == "12345":
            print("Acceso exitoso")
            print("Bienvenido al sistema")
        else:
            print("Código de área incorrecto")
    else:
        print("Contraseña incorrecta")
else:
    print("Correo incorrecto")
