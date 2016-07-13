import os
import sys
import time

def menu(a,b,c,l):
    print("OPERACION A REALIZAR")
    print()
    print("(1)....abono")
    print("(2)....retiro")
    print("(3)....prestamo")
    print("(4)....salir")
    print()
    while True:
        try:
            d=0
            while d<1 or d>4:
                d=int(input("su opcion es: "))
                if d<1 or d>4:
                    print()
                    print("opcion invalida")
                    print()
            break
        except  ValueError:
            print()
            print("opcion invalida")
            print()
    if d==1:
        k="abono"
        abono(a,b,c,d,k)

    elif d==2:
        k="retiro"
        retiro(a,b,c,d,k)

    elif d==3:
        k="prestamo"
        prestamo(a,b,c,d,k,l)

    elif d==4:
        os.system("clear")
        print()
        print("FIN DEL PROGRAMA")
        
def recibo(a,b,c,k):
    print()
    print("BANCO CONTINENTAL")
    print()
    print("nombres: ",a)
    print("DNI: ",b)
    print("operacion: ",k)
    print("saldo actual: ",c)

def continuar(a,b,c):
    print()
    g=input("desea continuar: ")
    if g.lower()=='si':
        menu(a,b,c)
    elif g.lower()=='no':
        print()
        print("fin de la operacion")
        seguir(a,b,c)
    
def seguir(a,b,c):
    f=str(input("desea realizar otra operacion: "))
    if f.lower()=='si':
        menu(a,b,c)
    elif f.lower()=='no':
        print()
        print("FIN DEL PROGRAMA")
          
def abono(a,b,c,d,k):
    while True:
        try:
            e=int(input("ingrese monto: "))
            break
        except ValueError:
            print("monto invalido")

    c=c+e
    recibo(a,b,c,k)
    continuar(a,b,c)

def retiro(a,b,c,d,k):
    while True:
        try:
            e=int(input("ingrese monto: "))
            break
        except ValueError:
            print("monto invalido")

    if e>c:
        print("su saldo es menor a la cantdad ingresada")
        menu(a,b,c)
    elif e<=c:
        c=c-e
        recibo(a,b,c,k)
        continuar(a,b,c)

def prestamo(a,b,c,d,k,l):
    while True:
        try:
            e=int(input("ingrese monto: "))
            break
        except ValueError:
            print("monto invalido")

    if l[0]=="2" and l[1]=="9":
        c=c+e*0.04
        recibo(a,b,c,k)
        continuar(a,b,c)

    else:
        c=c+e*0.03
        recibo(a,b,c,k)
        continuar(a,b,c)
    
    
