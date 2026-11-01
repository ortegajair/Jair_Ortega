class Cajero:

  def __init__(self, monto_inicial):
    self.monto = monto_inicial

  def retirar_dinero(self):
    cant_retiro = int(input("Ingresa el monto a retirar: "))

    if cant_retiro <= self.monto:
      self.monto -= cant_retiro
      return f"¡Retiro exitoso!\nEntregado: {cant_retiro}$.\nSaldo restante: {self.monto}$"
    else:
      return "Error: $ Fondos insuficientes $"

  def depositar_dinero(self):
    cant_deposito = float(input("Ingresa el monto a depositar: "))
    self.monto += cant_deposito
    return f"¡Depósito exitoso!\nNuevo saldo: {self.monto}$"

  def mostrar_saldo(self):
    return f"Tu saldo actual es de: {self.monto}$"


# Instancia del objeto
mi_cajero = Cajero(1000)

while True:
  print("\n       CAJERO DIGITAL  ")
  print("=" * 30)
  print("Bienvenido/a, ¿Qué haremos hoy?\n")
  print("1. Consultar saldo disponible")
  print("2. Depósito")
  print("3. Retiro")
  print("4. Salir")
  print("=" * 30)

  opcion = int(input("Selecciona una opción: "))

  if opcion == 1:
    print(mi_cajero.mostrar_saldo())
  elif opcion == 2:
    print(mi_cajero.depositar_dinero())
  elif opcion == 3:
    print(mi_cajero.retirar_dinero())
  elif opcion == 4:
    print("Saliendo.......")
    break  # Rompe el ciclo while y termina el programa
  else:
    print("Opción inválida. Intenta de nuevo.")