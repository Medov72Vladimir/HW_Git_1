import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Stopwatch stopwatch = new Stopwatch();
        Scanner scanner = new Scanner(System.in);

        int choice = 0;

        while (choice != 5) {
            System.out.println("1 - Start\n2 - Pause\n3 - Resume\n4 - Stop\n5 - Exit");
            System.out.print("Сделайте свой выбор: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    stopwatch.start();
                    break;
                case 2:
                    stopwatch.pause();
                    break;
                case 3:
                    stopwatch.resume();
                    break;
                case 4:
                    stopwatch.stop();
                    break;
                case 5:
                    System.out.println("Выход...");
                    break;
                default:
                    System.out.println("Неверный выбор. Пожалуйста, попробуйте еще раз.");
            }
        }
        System.out.println("Общее время работы секундомера: " + stopwatch.getElapsedTimeInMinutesAndSeconds());
        scanner.close();
    }
}
