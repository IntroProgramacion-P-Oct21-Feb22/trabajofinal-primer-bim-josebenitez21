numero1 = int(input("Ingresar un número: "))
numero2 = int(input("Ingresar un número: "))
numero3 = int(input("Ingresar un número: "))
if (numero1 == numero2 ) or (numero1 == numero3) or (numero2 == numero3):
    print("Ingresar valores diferentes, por favor")
else:
    print("El número mayor entre los valores {}, {} y {} es: {}".format(numero1, numero2, numero3,
                                                                max(numero1, numero2, numero3)))