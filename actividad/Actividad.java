/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package actividad;

import java.util.Scanner;

/**
 *
 * @author Sala de Sistemas
 */
public class Actividad {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Digite su nombre:");
        String nombre = entrada.nextLine();
        
        System.out.println("Digite su apellido:");
        String apellido = entrada.nextLine();
        
        System.out.println("Digite su edad:");
        int edad = entrada.nextInt();
        
        entrada.nextLine();
        System.out.println("Ingrese su sexo (Masculino/Femenino):");
        String sexo = entrada.nextLine();
        
        if(edad >= 18){
            System.out.println(nombre + " " + apellido + "es mayor de edad");
        }else{
            System.out.println(nombre + " " + apellido + " es menor de edad");
        }
        
        if(sexo.equalsIgnoreCase("masculino")){
            System.out.println(nombre + " Es un hombre.");
        }else{
            System.out.println("Es una mujer");
        }
}
    
}
