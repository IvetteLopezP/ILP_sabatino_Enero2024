#Ejercicio 1

#importar librerias o blibliotecas
import math
#Entrada de datos

calificación_1 = float(input("Primer parcial:"))
calificación_2 = float(input("Segundo parcial:"))
calificación_3 = float(input("Tercer parcial:"))

# Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.
#Procesos (Cálculos y operaciones matemáticas)

promedio = (calificación_1 + calificación_2 + calificación_3)/3

#Salida de datos
print("El promedio de 3 calificaciones =", round(promedio,1))

if (promedio >= 6 and promedio <=10):
   print("aprobado") 
elif (promedio <=6 and promedio >=0):
    print( "reprobado)")
elif (promedio <0 or promedio >10):
    print("Error")


