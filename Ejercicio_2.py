#Opereciones matemáticas

#Calcular el área de un circulo
#Entrada de datos
#Fórmula (Pi*radio)**2
#Declarar, crear instancias variables o constantes

radio = float(input("Ingresa un número:")) 
diámetro = float(input("ingresa un número"))
#Declarar constante
PI = 3.1416

#Procesos (Cálculos y operaciones matemáticas)

área = (PI * radio) ** 2
perímetro = (PI * diámetro)

#Salida de datos
print("El área del circulo es", round(área,1))
print("El perimetro de un circulo es", round(perímetro,1))
