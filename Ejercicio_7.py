#Ejericicio 7.
 #Pedir el nivel del agua en metros de una cisterna

#Declarar variables o constantes

#Entrada de Datos
nivel_de_agua= float(input("nivel de agua en metros:")) 

#Procesos (Cálculos y operaciones matemáticas)

if (nivel_de_agua > 6 ):     
    print("Desbordamiento de agua en cisterna")
elif (nivel_de_agua == 6 ):
     print("Apagar bomba")
elif (nivel_de_agua >= 5.9 and nivel_de_agua <= 4):     
    print("Desacelerar bomba")
elif (nivel_de_agua >=3.9 and nivel_de_agua <= 2):
    print("Bomba trabajando")
elif( nivel_de_agua >=1.9 and nivel_de_agua <=0):
    print("Acelerar bomba")
elif (nivel_de_agua == 0):
    print ("Encender bomba")
else : 
     print ("Fuga en cisterna")
