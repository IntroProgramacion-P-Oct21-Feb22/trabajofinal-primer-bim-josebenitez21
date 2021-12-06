a = "Triángulo Rectángulo"
b = "Triángulo Obtusángulo"
c = "Triángulo Acutángulo"
A = int(input ("Ingresar el valor del ángulo A: "))
B = int(input("Ingresar el valor del ángulo B: "))
C = int(input("Ingresar el valor del ángulo C: "))
if (A == 90) or (B == 90) or (C == 90):
            triangulo = a
else:
    if (A > 90) and (A < 180) or (B > 90) and (B < 180) or (C > 90) and (C < 180):
             triangulo = b
    else:
        triangulo = c
print("Los datos ingresados pertenecen a un:", triangulo)