import java.math.BigDecimal;

public class Kata
{

    public static String Factorial(int n) {
        BigDecimal bigDecimal = new BigDecimal(1);

        for (int i = 2; i <= n; i++) {
            bigDecimal = bigDecimal.multiply(new BigDecimal(i));
        }

        return bigDecimal.toString();
    }

}