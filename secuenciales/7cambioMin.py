"""
Author: Manuel Brito
Realiza un programa que reciba una cantidad de minutos y 
muestre por pantalla a cuantas horas y minutos corresponde.
"""

try:
    # Le pido al usuario la cantidad de minutos
    minutes = int(input("Dime la cantidad de minutos: "))
    
    # 1 hora es igual a 60 min, para hallar la cantidad de horas y minutos
    # divido los minutos entre 60 (para las horas) y el resto para 
    # los minutos sobrantes
    print(f"{minutes} minutos son {minutes // 60} horas y {minutes % 60} segundos")

except:
    print("ERR0R")






