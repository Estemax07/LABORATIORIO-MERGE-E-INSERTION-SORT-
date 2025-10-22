import java.util.Random;
public class QuickSort {
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int p = partition(arr, low, high);
            quickSort(arr, low, p);
            quickSort(arr, p + 1, high);
        }
    }
    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[(low + high) / 2];
        int i = low - 1;
        int j = high + 1;
        while (true) {
            do { i++; } while (arr[i] < pivot);
            do { j--; } while (arr[j] > pivot);
            if (i >= j) return j;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    public static void main(String[] args) {
        final int N = 100;          //tamaño de la lista (cambiar de 100 a 1000 a 10000 a 100000 a 1000000)
        final int REPS = 100;
        final int VAL_MAX = 10_000_000;
        Random rnd = new Random(42);
        int[] base = new int[N];
        for (int i = 0; i < N; i++) base[i] = rnd.nextInt(VAL_MAX);
        double[] tiempos = new double[REPS];
        System.out.println("\nSalida en 5 columnas (20 + 20 + 20 + 20 + 20)\n");
        System.out.printf("=== n=%d — QuickSort — %d ejecuciones ===%n", N, REPS);
        for (int r = 0; r < REPS; r++) {
            int[] arr = base.clone();
            long t0 = System.nanoTime();
            quickSort(arr, 0, arr.length - 1);
            long t1 = System.nanoTime();
            tiempos[r] = (t1 - t0) / 1_000_000_000.0;
        }
        System.out.printf("%-15s%-15s%-15s%-15s%-15s%n", "Col1", "Col2", "Col3", "Col4", "Col5");
        for (int row = 0; row < 20; row++) {
            for (int col = 0; col < 5; col++) {
                int idx = col * 20 + row;
                if (idx < REPS) System.out.printf("%4d: %.6f   ", idx + 1, tiempos[idx]);
                else System.out.print("                ");
            }
            System.out.println();
        }
        double suma = 0;
        for (double t : tiempos) suma += t;
        double promedio = suma / REPS;
        System.out.printf("%nPROMEDIO (%d) QuickSort n=%d: %.6f s%n", REPS, N, promedio);
    }
}
