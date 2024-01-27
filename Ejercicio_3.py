#Ejercicio 3

#importar librerias o blibliotecas
import math
#Entrada de datos
#Determinar la edad de una persona conociendo el año actual y el año de nacimiento.
#Declarar, crear instancias variables o constantes

año_nacimiento = float(input("Ingresa un número:")) 
año_actual = float(input("Ingresa otro número:"))

#Procesos (Cálculos y operaciones matemáticas)

edad = año_actual - año_nacimiento

#Salida de datos
print("Edad", round(edad, 1))