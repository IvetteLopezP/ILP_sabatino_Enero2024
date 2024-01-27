#Opereciones matemáticas

#importar librerias o blibliotecas
import math
#Entrada de datos

#Declarar, crear instancias variables o constantes
numero_1 = float(input("Ingresa un número:")) #Casteo: es la conversión de un tipo de dato a otro tipo de dato
numero_2 = float(input("Ingresa otro número:"))
#Declarar constante
PI = 3.1416

#Procesos (Cálculos y operaciones matemáticas)

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicación = numero_1 * numero_2
división = numero_1 / numero_2
potencia_1 = numero_1 ** numero_2
potencia_2 = pow(numero_1,numero_2) #Función (paramétros o orgumentos)
cuadrado = numero_1 ** 2
cubo = numero_2 ** 3
raiz_cuadrada_1 = math.sqrt (9)
raiz_cuadrada_2 = pow(27, 1/2)
raiz_cubica = pow (27, 1/3)

modulo_residuo = numero_1 % numero_2

#Salida de datos
print("La suma es =", suma)
print('La resta es =', resta)
print("La multiplicación es =", multiplicación)
print("La división es =", división)
print("La potencia 1 es =", round(potencia_1, 2))
print("La potencia 2 es = ", round(potencia_2, 2))
print("El módulo o residuo es =", modulo_residuo)
