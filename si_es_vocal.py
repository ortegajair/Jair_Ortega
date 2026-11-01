Vocales=["a","e","i","o","u"]
char=input("Ingresa un caracter: ")
char=char.lower()

if char in Vocales:
    print("Tu letra es una vocal")
else:
    print("Tu letra no es una vocal\nEs una consonante")