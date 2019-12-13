import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ThreadedCounting {
    static class Event {
        synchronized void set() { this.notifyAll(); }

        synchronized void await() {
            try { this.wait(); } catch (InterruptedException ignored) { }
        }
    }

    public static void countInThreads(Counter counter) {
        AtomicInteger i = new AtomicInteger();
        Event[] events = {new Event(), new Event(), new Event()};
        List<Integer> indexes = new ArrayList<>(Arrays.asList(2, 1, 2));

        IntStream.range(0, 3)
                .mapToObj(index -> new Thread(() -> {
                    while (true) {
                        events[index - 1 < 0 ? events.length - 1 : index - 1].await();

                        if (i.get() >= 100) {
                            events[index].set();
                            break;
                        }

                        counter.count(i.incrementAndGet());
                        events[index].set();
                    }
                }))
                .peek(Thread::start)
                .collect(Collectors.toList())
                .forEach(t -> {
                    try {
                        events[indexes.remove(0)].set();
                        t.join();
                    } catch (InterruptedException e) {}
                });
    }
}