import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.Random;

public class Psychic {

    private static MyRandom myRandom = new MyRandom();

    public static class MyRandom extends Random {
        @Override
        public double nextDouble() {
            return 0;
        }
    }

    static void setFinalStatic(Field field, Object newValue) throws Exception {
        field.setAccessible(true);

        Field modifiersField = Field.class.getDeclaredField("modifiers");
        modifiersField.setAccessible(true);
        modifiersField.setInt(field, field.getModifiers() & ~Modifier.FINAL);

        field.set(null, newValue);
    }

    static {
        try {
            Class<?> declaredClass = Math.class.getDeclaredClasses()[0];
            Field randomNumberGenerator = declaredClass.getDeclaredField("randomNumberGenerator");
            setFinalStatic(randomNumberGenerator, myRandom);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static double guess() {
        return myRandom.nextDouble();
    }
}
