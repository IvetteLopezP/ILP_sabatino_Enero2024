# Ejercicio 4 
# Pedir la cantidad de grados y convertirlos a °C, °F y K.

#Entrada de Datos
#Declarar variables o constantes
#Fórmulas:

c = float(input("Ingresa grados Celsius: ")) 
f = float(input("Ingresa grados Fahrenheit: "))
k = float(input("Ingresa grados Kelvin: "))

# Procesos
conversión_K_C = ( k - 273.15)
conversión_F_C = (5 * (f-32) / 9)
conversión_C_K = (c + 273.15)
conversión_K_F = ((9 * (k-273.15) / 5) + 32)
conversión_F_K = ((5 * (f - 32) / 9) + 273.15)
conversión_C_F = ((9 * c/5)+32)

# Salida
print ( "Kelvin a Celsius:", round(conversión_K_C,2))
print ( "Fahrenheit a Celsius:", round(conversión_F_C,2))
print ( "Celsuis a Kelvin: ", round(conversión_C_K,2))
print ("Kelvin a Fahrenheit:", round( conversión_K_F,2))
print ("Fahrenheit a Kelvin:", round(conversión_F_K,2))
print ("Celsius a Fahrenheit:", round(conversión_C_F,2))