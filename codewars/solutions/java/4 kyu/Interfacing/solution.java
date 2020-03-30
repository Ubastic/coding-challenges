import java.lang.reflect.Proxy;
import java.util.HashMap;

public class Interfacing {

    public static Object create(Class<?>[] interfaces) {
        HashMap<String, Object> attrs = new HashMap<>();

        return Proxy.newProxyInstance(interfaces[0].getClassLoader(), interfaces, (proxy, method, args) -> {
            String type = method.getName().substring(0, 3);
            String name = method.getName().substring(3);

            return type.equals("get") ? attrs.getOrDefault(name, null) : attrs.put(name, args[0]);
        });
    }

}