
import java.util.BitSet;
import java.util.stream.IntStream;
import java.util.function.IntSupplier;

public class Primes {
    public static IntStream stream() {
        return IntStream.generate(
                new IntSupplier() {
                    private final BitSet sieve = new BitSet();
                    private int max = 7;
                    private int next = 0;

                    public int getAsInt() {
                        if (next == 0) {
                            next = 1;
                            return 2;
                        } else if (next == 1) {
                            next = 2;
                            return 3;
                        }

                        int p = sieve.nextClearBit(next);
                        if (p > max) {
                            int m = (max << 1) + 1;
                            int s = sqrt(m);
                            for (int i = 2; i <= s; i++) {
                                if (!sieve.get(i)) {
                                    int n = n(i);
                                    int d = i & ~1;
                                    int j = i + (i - 1) * n;
                                    if (j <= max) j = max - (max - i) % n;
                                    boolean e = (j - i) / n % 2 == 0;
                                    for (; j > 0 && j <= m; j += n) {
                                        sieve.set(e ? j : j + d);
                                        e = !e;
                                    }
                                }
                            }
                            max = m;
                            p = sieve.nextClearBit(next);
                        }
                        next = p + 1;
                        return n(p);
                    }

                    int n(int b) {
                        return (b << 1) + (b & -2) - 1;
                    }

                    int sqrt(int b) {
                        double s = Math.sqrt(b * 3.0);
                        s += s % 2.0 < 1.0 ? 1.0 : 2.0;
                        return (int) (s / 3.0);
                    }
                }
        );
    }
}