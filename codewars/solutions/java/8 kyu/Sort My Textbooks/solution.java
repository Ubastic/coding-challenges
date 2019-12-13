import java.util.List;
import java.util.stream.Collectors;

class sorter {
    public static List<String> sort(List<String> textbooks) {
        return textbooks.stream().sorted(String::compareToIgnoreCase).collect(Collectors.toList());
    }
}