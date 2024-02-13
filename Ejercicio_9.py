#9.- Realizar un Menú de Opciones y realizar una función para cada opción:
#Entrada

#a) Mostrar una lista de 3 servicios de pasaje con sus estrellas de calificación

def Saludar():
  print("Hola, elige el tipo de pasaje")
def Terrestre():
  print ("pasaje terrestre")
def Aereo ():
  print ("pasaje aereo")
def Ferroviario ():
  print ("pasaje ferroviario")


print("*********** MENÚ DE OPCIONES / MÓDULOS ***************")
print("✌ 1. Saludo")
print("⭐⭐⭐🚌 2. terrestre")
print("⭐⭐⭐⭐⭐✈ 3. aereo")
print("⭐⭐⭐⭐🚉 4. ferroviario")

opción = int(input("Ingresa una opción: " ))

if (opción == 1):
  Saludar()   
elif (opción == 2):
  print("Terrestre")
elif (opción == 3):
  print("Aereo")
elif (opción == 4):
  print("Ferroviario")
else:
  print("Opción no válida")

#b) Calcular la nómina de un empleado en ENERO del 2024
#c) Generar una contraseña con el número de caracteres pedidos menor o igual a 5, si es mayor que 5 mostrar mensaje de error
#d) Pedir al usuario su nombre, primer ap., segundo ap. y edad e imprimir un saludo con sus datos








