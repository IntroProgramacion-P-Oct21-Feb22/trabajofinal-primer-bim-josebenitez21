cadena_1 = " "
base = 1

limite = float(input("Ingresar una medida en metros: "))
while(base <= limite):
    if(limite < 0):
        print("Solamente se permite valores positivos y números")

    yardas = (base * 1)/0.9144
    yardas = round(yardas,2)

    pulgadas = (base * 39.3701)/1
    pulgadas = round(pulgadas,2)

    pies = (base * 3.28084)/1
    pies = round(pies,2)

    cadena_1 = ("{}\n|     {}    |   {}   |   {}   |   {}   |"
            .format(cadena_1, base, yardas, pulgadas, pies))
    base+=1
cadena_2 = ("|  Metros  |  yardas  |  Pulgadas  |  Pies   |")
cadena_final = ("{}{}".format(cadena_2,cadena_1))
print(cadena_final)