import net.bytebuddy.ByteBuddy;
import net.bytebuddy.agent.ByteBuddyAgent;

import static net.bytebuddy.dynamic.loading.ClassReloadingStrategy.fromInstalledAgent;
import static net.bytebuddy.implementation.FixedValue.value;
import static net.bytebuddy.matcher.ElementMatchers.named;

public class Catch22 {
    static {
        ByteBuddyAgent.install();

        new ByteBuddy()
                .redefine(Yossarian.class)
                .method(named("isCrazy"))
                .intercept(value(Boolean.TRUE))
                .make()
                .load(Yossarian.class.getClassLoader(), fromInstalledAgent());
    }

    public static Yossarian loophole() {
        return new Yossarian() {};
    }
}