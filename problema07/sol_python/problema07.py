base = 2
suma = 0
numero_par = int(input("Ingrese un número par igual o mayor a 2: "))
if numero_par < 2 :
    print("Error\n Pruebe ingresar numeros iguales o mayores a 2")
if (numero_par % 2) != 0:
    print("El numero ingresado no es par, intenta nuevamente por favor.")

else:
     while(base <= numero_par):
        suma += base
        base += 2

print("La suma de los numeros pares es: {}".format(suma))