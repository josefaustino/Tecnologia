print("PROGRAMA DE CAJERO")
print()
while True:
    try:
        a=str(input("Nombres : "))
        break
    except ValueError:
        print("Ingrese nombre valido")
        print()

while True:
    try:
        p=0
        while p!=8:
            b=int(input("DNI : "))
            l=str(b)
            p=len(l)
            if p!=8:
                print()
                print("ingrese 8 cifras")
                print()
        break
    except ValueError:
        print()  
        print("Ingrese DNI valido")
        print()      
while True:
    try:
        c=int(input("Saldo actual : ")) 
        break
    except ValueError:
        print()
        print("Ingrese una cantidad")
        print()
from moduexam import menu

menu(a,b,c,l)
