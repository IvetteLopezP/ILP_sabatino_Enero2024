#Condicionales. Mayor o menor de edad
#Entrada de datos
#Declarar la variable
edad = int(input("Ingresa tu edad:"))

#PROCESO
if (edad >= 18 and edad <= 120):     #Rango de edad (18 hasta 120)
    print("Mayor de edad")
elif (edad >= 0  and edad <18):     #Rango de edad (0 hasta 18)
    print("Menor de edad")
elif (edad < 0 or edad > 120):      #Edad sea menor que 0 o mayor 120
    print("Error")