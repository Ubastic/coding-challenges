import java.util.*;
import java.util.stream.IntStream;

public class Primes {
    private static Map<Integer, Boolean> isPrimeMap = new HashMap<>();

    public static boolean isPrimeInner(int n) {
        if ((n > 2 && n % 2 == 0) || n == 1) {
            return false;
        }

        for (int i = 3; i <= (int) Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static boolean isPrime(int value) {
        if (isPrimeMap.containsKey(value)) {
            return isPrimeMap.get(value);
        }
        boolean result = isPrimeInner(value);
        isPrimeMap.put(value, result);

        return result;
    }


    public static int nextPrime(int i) {
        return IntStream.iterate(i + 1, ii -> ii + 1).filter(Primes::isPrime).findFirst().orElse(0);
    }

    public static IntStream stream() {
        return IntStream.iterate(2, Primes::nextPrime);
    }
}
