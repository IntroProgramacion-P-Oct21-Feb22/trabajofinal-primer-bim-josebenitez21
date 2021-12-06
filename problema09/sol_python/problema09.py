signo = ""
signo1 = "-"
signo2 ="+"
cadenaFinal = ""
numero1 = 12
numero2 = 11
limite=48
limite2=44
while(numero2 <= limite2) or (numero1 <= limite):

    cadenaFinal = "{} {}{} {}{}".format(cadenaFinal, signo2, numero1, signo1, numero2)
    numero1 = numero1 + 12
    numero2 = numero2 + 11
    if(numero1 % 12 == 0):
        signo= signo2
    else:
        if(numero2 == 11 or numero2 % 11 == 0):
            signo=signo1

print(cadenaFinal)