/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problema07;

import java.util.Scanner;
import java.util.Locale;

/**
 *
 * @author USUARIO
 */
public class Problema07 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);
        int numero_par;
        int resultado;
        int contador = 0;
        System.out.println("Ingrese un numero par");
        numero_par = entrada.nextInt();

        if (numero_par < 2) {
            System.out.println("El número no se encuentra en el rango permitido");
        } else {
            if (numero_par % 2 != 0) {
                System.out.println("El número ingresado no es par");
            } else {
                resultado = numero_par + 2;
                while (resultado <= numero_par) {
                    resultado = resultado + 2;

                }
                System.out.println("La suma de los números pares es:" + resultado);
            }

        }

    }

}
