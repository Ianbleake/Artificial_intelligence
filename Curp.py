def extraer_consonantes(cadena):

    consonantes = ""
    for caracter in cadena:
        if caracter.isalpha() and caracter.lower() not in 'aeiouAEIOU':
            consonantes += caracter
    return consonantes

def extraer_vocales(cadena):
    vocales = ""
    for caracter in cadena:
        if caracter.isalpha() and caracter.lower() not in 'qwrtypñlkjhgfdszxcvbnmQWRTYPÑLKJHGFDSZXCVBNM':
            vocales += caracter
    return vocales


def consulta(curp):
    print("Consulta:")
    archi1=open("CURPS.txt","r")
    lineas=[]
    linea=archi1.readline()
    lineas.append(linea)
    while linea!='':
        print(end='')
        linea=archi1.readline()
        lineas.append(linea)
    resultado=[]
    for x in lineas:
        
        print(busca)
        if curp==busca:
           resultado.append(x)
    
   
    print(resultado)
    print(curp.upper())



def guardar(curp):
    print("Se guardo:")
    guardar = open('CURPS.txt','a')
    guardar.write("\n")
    guardar.write(curp.upper())
    guardar.write("\n")
    guardar.close()

    print(curp.upper())

def asignacion(curp):
    c1=0
    c2=0
    archi1=open("CURPS.txt","r")
    lineas=[]
    linea=archi1.readline()
    lineas.append(linea)
    while linea!='':
        print(end='')
        linea=archi1.readline()
        lineas.append(linea)
    #a este punto lineas ya tiene todas las lineas del txt
    #se ectraenb los ultimos dos digitos
    bandera=False
    for x in lineas:
        busca=x[:-3]
        if curp==busca:
            c1=x[-3]
            c2=x[-2]
            bandera=True
        

    c1=int(c1)
    c2=int(c2)
    #ya tenemos los ultimos dos valores
    if(c2==9):
        c2=0
        c1+=1
    else:
        c2+=1
    archi1.close()
    if bandera==False:
        c1=0
        c2=0
    c1=str(c1)
    c2=str(c2)
    curp=curp+c1+c2

    return(curp)

groserias=["CULO","COLA","PENE","PITO",]
entDict={"1":"as","2":"BS","3":"CL","4":"CS","5":"DF","6":"GT","7":"HG","8":"MC","9":"MS","10":"NL","11":"PL","12":"QR","13":"SL","14":"TC","15":"TL","16":"YN","17":"BC","18":"CC","19":"CM","20":"CH","21":"DG","22":"GR","23":"JC","24":"MN","25":"NT","26":"OC","27":"QT","28":"SP","29":"SR","30":"TS","31":"VZ","32":"ZS"}

control=input("Que desea hacer? \n 1.-Consultar \n 2.-Registrar \n")
"""
print("Ingrese su primer nombre:")
nombre=input()
print("Ingrese su segundo nombre:")
nombre2=input()
print("Ingrese su primer apellido:")
apellido=input()
print("Ingrese su segundo apellido:")
apellido2=input()
print("Ingrese su fecha de nacimiento(AAMMDD):")
fecha=input()
print("Ingrese su lugar de nacimiento")
print("1.-Aguascalientes 2.-B.California Sur 3.-Coahuila 4.-Chiapas \n 5.-CDMX 6.-Guanajuato 7.-Hidalgo 8.-Edo.MX \n 9.-Morelos 10.-Nuevo Leon 11.-Puebla 12.-Quintana Roo \n 13.-Sinaloa 14.-Tabasco 15.-Tlaxcala 16.-Yucatan \n 17.-B.California 18.-Campeche 19.-Colima 20.-Chihuahua \n 21.-Durango 22.-Guerrero 23.-Jalisco 24.-Michoacan \n 25.-Nayarit 26.-Oaxaca 27.-Queretaro 28.-San Luis Potosi \n 29.-Sonora 30.-Tamaulipas 31.-Veracruz 32.-Zacatecas")
lugar=input()
nacio=entDict[lugar]
print("Ingrese su sexo:")
sexo=input()

Cnombre=extraer_consonantes(nombre)
Capellido=extraer_consonantes(apellido)
Capellido2=extraer_consonantes(apellido2)

Vnombre=extraer_vocales(nombre)
Vapellido=extraer_vocales(apellido)
Vapellido2=extraer_vocales(apellido2)

curp=apellido[0]+Vapellido[0]+apellido2[0]+nombre[0]+fecha+sexo[0]+nacio+Capellido[1]+Capellido2[1]+Cnombre[0]
"""
curp="RAVA990929HDGNZN"
if control=='1':
    consulta(curp)

elif control=='2':
    curp=asignacion(curp.upper())
    guardar(curp)