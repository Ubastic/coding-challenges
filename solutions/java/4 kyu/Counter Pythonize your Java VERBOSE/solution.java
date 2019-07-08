import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Counter<T> extends HashMap<T, Long> {

    public Counter(Map<? extends T, Long> map) {
        this.putAll(map);
    }

    @SafeVarargs
    public Counter(Object... arr) {
        this(Arrays.stream(arr));
    }

    public Counter(int initialCapacity, float loadFactor) {
        super(initialCapacity, loadFactor);
    }

    public Counter(Collection<? extends T> coll) {
        this(coll.stream());
    }

    public Counter(Stream<?> stream) {
        stream.forEach(i -> put((T) i, getOrDefault(i, 0L) + 1));
    }

    private Stream<SimpleEntry<T, Long>> pairStream(Counter<? extends T> c, Function<T, Long> mergeFunction) {
        return keyStream(c).map(a -> new SimpleEntry<>(a, mergeFunction.apply(a)));
    }

    private Stream<T> keyStream(Counter<? extends T> c) {
        return Stream.concat(keySet().stream(), c.keySet().stream()).distinct();
    }

    static public Counter<Boolean> of(boolean... arr) {
        Counter<Boolean> counter = new Counter<>();
        counter.pushAll(counter, arr);

        return counter;
    }

    static public Counter<Character> of(char... arr) {
        Counter<Character> counter = new Counter<>();
        counter.pushAll(counter, arr);

        return counter;

    }

    static public Counter<Double> of(double... arr) {
        Counter<Double> counter = new Counter<>();
        counter.pushAll(counter, arr);

        return counter;
    }

    static public Counter<Float> of(float... arr) {
        Counter<Float> counter = new Counter<>();
        counter.pushAll(counter, arr);

        return counter;
    }

    static public Counter<Byte> of(byte... arr) {
        Counter<Byte> counter = new Counter<>();
        counter.pushAll(counter, arr);

        return counter;
    }

    static public Counter<Integer> of(int... arr) {
        Counter<Integer> counter = new Counter<>();
        counter.pushAll(counter, arr);

        return counter;
    }

    static public Counter<Long> of(long... arr) {
        Counter<Long> counter = new Counter<>();
        counter.pushAll(counter, arr);

        return counter;
    }

    static public Counter<Short> of(short... arr) {
        Counter<Short> counter = new Counter<>();
        counter.pushAll(counter, arr);

        return counter;
    }

    static public Counter<String> of(String arr) {
        Counter<String> counter = new Counter<>();
        counter.pushAll(counter, arr);

        return counter;
    }

    @Override
    public String toString() {
        return "Counter(" + super.toString() + ")";
    }

    public Long get(Object key) {
        return getOrDefault(key, 0L);
    }

    public Stream<T> elements() {
        return entrySet().stream().flatMap(entry ->
                Stream.iterate(entry.getKey(), i -> entry.getKey()).limit(entry.getValue() > 0 ? entry.getValue() : 0)
        );
    }

    public List<T> elementsAsList() {
        return elements().collect(Collectors.toList());
    }

    public Stream<Map.Entry<T, Long>> mostCommon() {
        return entrySet().stream().sorted((o1, o2) -> o2.getValue().compareTo(o1.getValue()));
    }

    public Stream<Map.Entry<T, Long>> mostCommon(long n) {
        return mostCommon().limit(n);
    }

    public List<Map.Entry<T, Long>> mostCommonAsList() {
        return mostCommon().collect(Collectors.toList());
    }

    public List<Map.Entry<T, Long>> mostCommonAsList(long n) {
        return mostCommon(n).collect(Collectors.toList());
    }

    public void push(T key) {
        push(key, 1L);
    }

    public void push(T key, long n) {
        put(key, getOrDefault(key, 0L) + n);
    }

    public void pushAll(Stream<? extends T> stream) {
        stream.forEach(this::push);
    }

    public void pushAll(Collection<? extends T> coll) {
        coll.forEach(this::push);
    }

    public void pushAll(T[] arr) {
        Arrays.stream(arr).forEach(this::push);
    }

    public void pushAll(Map<? extends T, Long> other) {
        other.forEach(this::push);
    }

    public static void pushAll(Counter<Boolean> cnt, boolean[] arr) {
        for (Boolean i : arr) {
            cnt.push(i);
        }
    }

    public static void pushAll(Counter<Byte> cnt, byte[] arr) {
        for (Byte i : arr) {
            cnt.push(i);
        }
    }

    public static void pushAll(Counter<Character> cnt, char[] arr) {
        for (Character i : arr) {
            cnt.push(i);
        }
    }

    public static void pushAll(Counter<Double> cnt, double[] arr) {
        for (Double i : arr) {
            cnt.push(i);
        }
    }

    public static void pushAll(Counter<Float> cnt, float[] arr) {
        for (Float i : arr) {
            cnt.push(i);
        }
    }

    public static void pushAll(Counter<Integer> cnt, int[] arr) {
        for (Integer i : arr) {
            cnt.push(i);
        }
    }

    public static void pushAll(Counter<Long> cnt, long[] arr) {
        for (Long i : arr) {
            cnt.push(i);
        }
    }

    public static void pushAll(Counter<Short> cnt, short[] arr) {
        for (Short i : arr) {
            cnt.push(i);
        }
    }

    public static void pushAll(Counter<String> cnt, String s) {
        for (Character i : s.toCharArray()) {
            cnt.push(String.valueOf(i));
        }
    }

    public Counter<T> add(Counter<? extends T> c) {
        return new Counter<>(
                pairStream(c, key -> get(key) + c.get(key))
                        .filter(entry -> entry.getValue().compareTo(0L) > 0)
                        .collect(Collectors.toMap(SimpleEntry::getKey, SimpleEntry::getValue))
        );
    }

    public Counter<T> sub(Counter<? extends T> c) {
        return new Counter<>(
                pairStream(c, key -> get(key) - c.get(key))
                        .filter(entry -> entry.getValue().compareTo(0L) > 0)
                        .collect(Collectors.toMap(SimpleEntry::getKey, SimpleEntry::getValue))
        );
    }

    public Counter<T> intersect(Counter<? extends T> c) {
        return new Counter<>(
                keySet()
                        .stream()
                        .filter(c::containsKey)
                        .filter(key -> (get(key) > 0 && c.get(key) > 0) || (get(key) < 0 && c.get(key) < 0))
                        .collect(Collectors.toMap(key -> key, key -> Math.min(get(key), c.get(key))))
        );
    }

    public Counter<T> union(Counter<? extends T> c) {
        return new Counter<>(
                pairStream(c, key -> Math.max(get(key), c.get(key)))
                        .filter(entry -> !entry.getValue().equals(0L))
                        .collect(Collectors.toMap(SimpleEntry::getKey, SimpleEntry::getValue))
        );
    }

    public Counter<T> subtract(Counter<? extends T> c) {
        return new Counter<>(pairStream(c, key -> get(key) - c.get(key))
                .collect(Collectors.toMap(SimpleEntry::getKey, SimpleEntry::getValue))
        );
    }

    public Counter<T> mul(int n) {
        Counter<T> counter = new Counter<>();
        forEach((key, value) -> counter.put(key, value * n));
        return counter;
    }

}
