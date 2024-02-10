#Ejercicio 6
#6. Pedir un número y decir si es par o impar.

#Declarar variables o constantes

#Entrada de Datos
número = float(input("Ingresa un número:")) 

#Procesos (Cálculos y operaciones matemáticas)
par = (número % 2 == 0)
impar = ( número % 2 != 0)

#Salida

print("Es un número par:", par)
print("Es un número impar:", impar)


