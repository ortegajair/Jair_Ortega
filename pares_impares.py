num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))


if num1 %2 ==0 and num2 %2 ==0:
    print("Ambos numeros son PARES")
elif num1 %2 !=0 and num2 %2 !=0:
    print("Ambos numeros son IMPARES") 
elif num1 %2 ==0 and num2 %2 !=0:
    print("El primer numero es par\nEl segundo es IMPAR")
else:
    print("El primer numero es impar\nEl segundo es PAR")        
    