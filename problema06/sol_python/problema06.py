numerador = 1
denominador = 1
division_suma = 0;
while ( denominador < 100):
    resultado = numerador/denominador
    denominador += 1
    print("+{}/{}".format(numerador, denominador))
    division_suma = division_suma + resultado
print("El resultado obtenido de la suma de las fracciones es: %.2f\n" %(division_suma))