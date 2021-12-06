pago_extra= 0

nombre = input("Ingresar el nombre del empleado: ")

tipo_empleado = int(input("Ingresar el tipo de empleado (solo se "
                   + "admite un número: : 1 , 2 , 3 o 4): "))

# Solo se admite horas, por lo tanto será un valor entero

horas_trabajadas=int(input("Ingresar el número de horas extras laboradas: "))


if (tipo_empleado == 1) :
    cuota_hora = 1.5
    pago_extra = horas_trabajadas * cuota_hora

else :
    if (tipo_empleado == 2) :
        cuota_hora = 2
        pago_extra = horas_trabajadas * cuota_hora

    else:
        if  (tipo_empleado == 3) :
            cuota_hora = 2.5
            pago_extra = horas_trabajadas * cuota_hora

        else :
            if (tipo_empleado == 4) :
                cuota_hora = 3
                pago_extra = horas_trabajadas * cuota_hora

print("El pago por las horas trabajadas es: ", pago_extra)