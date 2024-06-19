#evaluacion3
import csv

Trabajadores=[]
Personas=[]
Cargos=["CEO","ANALISTA","PROGRAMADOR"]
SueldoBruto=[]
Liquido=[]

def desc(salud):
    Liquido = SueldoBruto-70000
    
def desc(AFP):
    Liquido = SueldoBruto-120000

while True:
    print("-"*25)
    print("1.Trabajadores.")
    print("2.Sueldos.")
    print("3.Salir del Programa")
    print("-"*25)
    opc=int(input("Ingrese una opcion:>>"))
    
    match opc:
        case 1:
            print("Que desea hacer?")
            print("1.Ingresar Trabajadores.")
            print("2.Imprimir Trabajadores.")
            print("3.Volver Menu.")

            opc2=int(input(">>>"))
            if opc2 ==1:
                    Personas=input("Ingrese El trabajador con Nombre y Apellido:")
                    Trabajadores.append(Personas)
                    
            if opc2 ==2:
                        print(Trabajadores)
            if opc2 ==3:
                print("Has Vuelto al MENU")