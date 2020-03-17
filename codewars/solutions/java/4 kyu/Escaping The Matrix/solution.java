class AgentSmith {
    public static <T extends Exception> void fight(Exception e) throws T {
        throw (T) e;
    }
}

public class Matrix {
    public static void enter() {
        AgentSmith.fight(new Neo());
    }
}