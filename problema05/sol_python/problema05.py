x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

if (x > 0 and y > 0) :
    print("Los valores corresponden al Primer Cuadrante")
else:
    if(x < 0 and y > 0):
        print("Los valores corresponden al Segundo Cuadrante")
    else:
        if(x < 0 and y < 0):
            print("Los valores corresponden al Tercer Cuadrante")
        else:
            print("Los valores corresponden al Cuarto Cuadrante")
