
#Ejercicio 5
#Obtener valores para: a, b y c. Calcular la fórmula general.

#importar librerias o blibliotecas
import math
#Declarar variables o constantes
#Fórmulas:
# x1 = (- b- Raíz cuadrada de b*2-4ac/2a), x2 = (- b + Raíz cuadrada de b*2-4ac/2a)

#Entrada de Datos
a = float(input("Ingresa el valor de a:")) 
b = float(input("Ingresa el valor de b:"))
c = float(input("Ingresa el valor de c:"))

#Procesos (Cálculos y operaciones matemáticas)

x1 = (- b - math.sqrt (b * 2 - (4 * a * c) / (2 * a)))
x2 = (- b + math.sqrt (b * 2 - (4 * a * c) / (2 * a)))

#Salida
print("Valor de X1", round(x1, 1))
print("Valor de X2", round(x2, 1))
