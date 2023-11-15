public class Stopwatch {
    private long startTime;
    private long pauseTime;
    private boolean isRunning;

    public Stopwatch() {
        startTime = 0;
        pauseTime = 0;
        isRunning = false;
    }

    public void start() {
        if (!isRunning) {
            startTime = System.currentTimeMillis();
            isRunning = true;
            System.out.println("Секундомер запущен");
        } else {
            System.out.println("Секундомер уже работает");
        }
    }

    public void pause() {
        if (isRunning) {
            pauseTime = System.currentTimeMillis();
            isRunning = false;
            System.out.println("Секундомер на паузе. Время: " + getElapsedTimeInMinutesAndSeconds());
        } else {
            System.out.println("Секундомер уже на паузе");
        }
    }

    public void resume() {
        if (!isRunning) {
            long elapsedTime = System.currentTimeMillis() - pauseTime;
            startTime += elapsedTime;
            isRunning = true;
            System.out.println("Секундомер запущен");
        } else {
            System.out.println("Секундомер уже работает");
        }
    }

    public void stop() {
        if (isRunning) {
            isRunning = false;
            System.out.println("Секундомер остановлен. Время: " + getElapsedTimeInMinutesAndSeconds());
        } else {
            System.out.println("Секундомер уже остановлен");
        }
    }

    public String getElapsedTimeInMinutesAndSeconds() {
        long elapsedTime = System.currentTimeMillis() - startTime;
        long minutes = (elapsedTime / 1000) / 60;
        long seconds = (elapsedTime / 1000) % 60;
        return String.format("%d:%02d", minutes, seconds);
    }
}
