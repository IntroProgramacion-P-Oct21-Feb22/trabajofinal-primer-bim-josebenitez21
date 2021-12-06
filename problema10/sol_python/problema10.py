varianza = 0
desviaciones = 0
bandera = True
media = 0
suma = 0
suma_desviaciones = 0
lista = []


while (bandera):
    num = float(input("Ingresar el dato a ser calculado: "))
    lista.append(num)

    pregunta_salida = input("Desea ingresar otro dato: [Si][No]: ")
    if pregunta_salida == "SI" or pregunta_salida == "Si" or pregunta_salida == "Si":
        print()
    else:
        bandera = False;
        cantidadvalor = len(lista)

        for num in range(len(lista)):
            suma = suma + lista[num]
        media = suma / cantidadvalor

        for num in range(len(lista)):
            suma_desviaciones = suma_desviaciones + ((lista[num] - media) ** 2)
        varianza = suma_desviaciones / cantidadvalor

print("El valor de la media obtenido es: {}".format(media))
print("El valor de varianza final obtenido es: {}".format(varianza))