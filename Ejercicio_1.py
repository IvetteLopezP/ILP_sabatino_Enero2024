#Ejercicio 1

#importar librerias o blibliotecas
import math
#Entrada de datos

# Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

calificación_1 = float(input("Primer parcial:"))
calificación_2 = float(input("Segundo parcial:"))
calificación_3 = float(input("Tercer parcial:"))
#Procesos (Cálculos y operaciones matemáticas)

promedio = (calificación_1 + calificación_2 + calificación_3)/3

#Salida de datos
print("El promedio de 3 calificaciones =", round(promedio,1))

