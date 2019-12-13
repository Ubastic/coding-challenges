public class SetStuff {

    public static java.util.Set<int[]> cartesianProduct(int[][] sets) {
        return sets.length == 0 ? new java.util.HashSet<>() :
                java.util.Arrays.stream(sets[0])
                        .boxed()
                        .flatMap(i ->
                                java.util.Optional.ofNullable(
                                        cartesianProduct(java.util.Arrays.copyOfRange(sets, 1, sets.length))
                                )
                                        .map(s -> s.size() == 0 ? java.util.Collections.singleton(new int[]{}) : s)
                                        .map(s -> s
                                                .stream()
                                                .map(arr -> java.util.stream.Stream
                                                        .concat(java.util.stream.Stream.of(i), java.util.Arrays.stream(arr).boxed())
                                                        .mapToInt(j -> j)
                                                        .toArray()
                                                )
                                        ).get()
                        ).collect(java.util.stream.Collectors.toSet());
    }
}
