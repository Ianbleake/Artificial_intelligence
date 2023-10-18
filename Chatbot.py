#inicialización de estados 
import re
import time


 # Lenguaje natural por expresiones regulares 
Promo_RE = r"promociones|promos?|descuentos"
Cita_RE = r"cita|servicio|agendar"
Venta_RE = r"venta|comprar|venden"
placa_Re = r"\d\d\d[\s| |-]?\w\w\w" 
afirmacion_RE = r"s[i|í]|claro|definitavamente"





state=0
Salida=1
while Salida:
    if state==0:
        print("Hola soy el Chatbot de la FORD ¿En qué te puedo ayudar?")
        time.sleep(1)
        opcion=input("Soy capaz de informarte de nuestras promociones, venta de vehículos y ayudarte a agendar un cita. \n\t\t\t")
        if re.findall(Promo_RE, opcion, flags=0)!=[]:
            state=1
        elif re.findall(Cita_RE, opcion, flags=0)!=[]: 
            state=2
        elif re.findall(Venta_RE, opcion, flags=0)!=[]:  
            state=3
    if state == 1:
        print("Nuestras promociones son...")
        state=6
    if state == 2:
        name = input("Dime tu nombre para agendar la cita. \n\t\t\t")
        state = 4
    if state == 3:
        print("En un momento te contactara un agente de ventas")
        Salida=0
    if state == 4:
        placa = input("Podrias proporcionarme tu placa. \n\t\t\t")
        if re.findall(placa_Re, placa, flags=0)!=[]:
            state = 5
        else:
            print("Placa Invalida")
    if state == 5:
        print("Gracias {} en un momento te atendera un operador".format(name))
        Salida=0
    if state == 6:
        opcion=input("¿te puedo ayudar en algo más?  \n\t\t\t")
        if re.findall(afirmacion_RE, opcion, flags=0!=[]):
            state=0
        else:
            print("Gracias fue un placer atenderte")
Salida=0