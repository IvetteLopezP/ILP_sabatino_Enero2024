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

#Declarar variables o constantes

#Entrada de Datos

días_laborados = 31
pago_día = 280
iva =  0.16
isr =  0.18
#Procesos (Cálculos y operaciones matemáticas)

pago_base = (días_laborados * pago_día)
iva_trasladado = (pago_base * iva)
subtotal= (pago_base + iva_trasladado)
iva_retenido = (iva_trasladado * 2/3)
isr_retenido = (pago_base * isr)
pago_neto = (subtotal - iva_retenido) - (isr_retenido)

#Salida

def mostrar_pago_base():
    print("El pago base es =", round(pago_base_calculado, 2))

def mostrar_iva_trasladado():
    print("El IVA trasladado es =", round(iva_trasladado_calculado, 2))

def mostrar_subtotal():
    print("El subtotal es =", round(subtotal_calculado, 2))

def mostrar_iva_retenido():
    print("El IVA retenido es =", round(iva_retenido_calculado, 2))

def mostrar_isr_retenido():
    print("El ISR retenido es =", round(isr_retenido_calculado, 2))

def mostrar_pago_neto():
    print("El pago neto es =", round(pago_neto_calculado, 2))

print("*********** MENÚ DE OPCIONES / MÓDULOS ***************")
print(" 1. pago base")
print(" 2. IVA trasladado")
print(" 3. Subtotal")
print(" 4. IVA retenido")
print(" 5. ISR retenido")
print(" 6. Pago nómina enero 2024")
opción = int(input("Ingresa una opción: " ))
  
if opción == 1:
    mostrar_pago_base()
elif opción == 2:
    mostrar_iva_trasladado()
elif opción == 3:
    mostrar_subtotal()
elif opción == 4:
    mostrar_iva_retenido()
elif opción == 5:
    mostrar_isr_retenido()
elif opción == 6:
    mostrar_pago_neto()
else:
  print("Opción no válida")

#c) Generar una contraseña con el número de caracteres pedidos menor o igual a 5, si es mayor que 5 mostrar mensaje de error
#d) Pedir al usuario su nombre, primer ap., segundo ap. y edad e imprimir un saludo con sus datos








