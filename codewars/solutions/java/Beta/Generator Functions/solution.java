import java.util.Optional;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.function.Consumer;

public class GeneratorFunction<I, O> {

    final Consumer<I> func;

    public GeneratorFunction(Consumer<I> func) {
        this.func = func;
    }

    public GeneratorFunction(Runnable func) {
        this.func = ignored -> func.run();
    }

    public Generator<I, O> call() {
        return new Generator<>(func);
    }

}

class Generator<I, O> {
    volatile private boolean finished = false;

    static final ThreadLocal<Generator> current = new ThreadLocal<>();

    final BlockingQueue<Optional<I>> in = new ArrayBlockingQueue<>(1);
    final BlockingQueue<Optional<O>> out = new ArrayBlockingQueue<>(1);

    Generator(Consumer<I> func) {
        Thread thread = new Thread(() -> {
            current.set(this);
            try {
                func.accept(in.take().orElse(null));
                finished = true;
                out.put(Optional.empty());
            } catch (InterruptedException e) {
            }
        });
        thread.setDaemon(true);
        thread.start();
    }

    static <I, O> Generator<I, O> get() {
        return (Generator<I, O>) current.get();
    }

    public O next(I arg) {
        try {
            in.put(Optional.ofNullable(arg));
            return out.take().orElse(null);
        } catch (InterruptedException e) {
        }
        return null;
    }

    public O next() {
        return next(null);
    }

    public boolean done() {
        return finished;
    }
}

class Flow {

    public static <I, O> I yield(O result) {
        try {
            Generator<I, O> gen = Generator.get();
            gen.out.put(Optional.ofNullable(result));
            return gen.in.take().orElse(null);
        } catch (InterruptedException e) {
        }
        return null;
    }

    public static <I, O> void yieldFrom(GeneratorFunction<I, O> func) {
        func.func.accept(null);
    }

}