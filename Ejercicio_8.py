#Calcular la nómina para un empleado en el mes de Mayo del 2023 conociendo
#su pago por día de $250.-

#Declarar variables o constantes

#Entrada de Datos

días_laborados = 31
pago_día = 250
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
print ("Nomina mayo 2023:", round(pago_neto,2))

