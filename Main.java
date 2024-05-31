import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese la cantidad de estaciones de trabajo: ");
        int n = scanner.nextInt();
        scanner.nextLine(); // Consumir el salto de línea después de leer n

        EstacionTrabajo[] estaciones = new EstacionTrabajo[n];
        int acumuladoCosto = 0;
        int estacionesTipo1 = 0;

        for (int i = 0; i < n; i++) {
            System.out.println("Estación de trabajo #" + (i + 1));

            System.out.print("Ingrese la cantidad de unidades producidas: ");
            int cantidadUnidades = scanner.nextInt();

            System.out.print("Ingrese el tipo de unidades (1 o 2): ");
            int tipoUnidades = scanner.nextInt();

            estaciones[i] = new EstacionTrabajo(cantidadUnidades, tipoUnidades);
            acumuladoCosto += estaciones[i].calcularCostoProduccion();

            if (estaciones[i].getTipoUnidades() == 1) {
                estacionesTipo1++;
            }

            System.out.println();
        }

        System.out.println("Costo acumulado de todas las estaciones de trabajo: $" + acumuladoCosto);
        System.out.println("Cantidad de estaciones de trabajo con producción de unidades tipo 1: " + estacionesTipo1);

        scanner.close();
    }
}
