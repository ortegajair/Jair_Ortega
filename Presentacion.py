# Logo compacto para evitar problemas de alineación en la terminal
logo = r"""
  __  __   __   __
 |  \/  |  \ \ / /
 | \  / |   \ V / 
 | |\/| |    | |  
 | |  | |    | |  
 |_|  |_|    |_|  

  ___  ___  ____ ___ _____ _  _ _____  _  _____ ___ ___  _  _ 
 | _ \| _ \/ __| _ \ __| \| |_   _|/ \|_   _|_ _/ _ \| \| |
 |  _/|   /\__ \  _/ _|| .` | | | / _ \ | |  | | (_) | .` |
 |_|  |_|_\|___/_| |___|_|\_| |_|/_/ \_\|_| |___\___/|_|\_|
"""

print(logo)

cohete = r"""
           /\
          /  \
         |    |
         |    |
        /| == |\
       / | == | \
      |  |====|  |
      |  |  * |  |
     /   | == |   \
    /    |____|    \
   '======'    '======'
       \  /    \  /
        \/      \/
        (░░▒▒▓▓█)
       (░░▒▒▓▓███)
      (░░▒▒▓▓█████)
"""

print(cohete)


def menu():
    while True:
        print("\n" + "=" * 45)
        print("    --- ¿Qué te gustaría saber sobre mí? ---")
        print("=" * 45)
        print("1. Información básica")
        print("2. Mis favoritos (colores, comida, país)")
        print("3. Mis pasatiempos")
        print("4. Salir")
        print("=" * 45 + "\n")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            print(
                "\nMi nombre es Jair, tengo 17 años y soy estudiante de Informática."
            )
        elif opcion == "2":
            print(
                "\nMis colores favoritos son: azul y negro"
                "\nMi comida favorita es: seco de pollo"
                "\nMi país favorito es: Francia"
            )
        elif opcion == "3":
            print(
                "\nEn mi tiempo libre, me gusta entrenar en el gimnasio, jugar al fútbol y escuchar música."
            )
        elif opcion == "4":
            print("\n¡Ahora conoces un poco más sobre mí! Nos vemos luego.")
            break
        elif opcion == "030709":
            print("\n¡DATO OCULTO DESBLOQUEADO!")
            print("Tengo una gata de mascota, su nombre es Susi 🐾")
        
        else:
            print("\nOpción no válida, por favor intenta de nuevo.")

        input("\n[Presiona Enter para continuar...]")


menu()