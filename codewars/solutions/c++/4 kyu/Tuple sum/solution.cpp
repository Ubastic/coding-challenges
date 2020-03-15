template<typename Tuple, typename F, std::size_t ...Indices>
void for_each_impl(Tuple &&tuple, F &&f, std::index_sequence<Indices...>) {
    auto _ = {0, (f(std::get<Indices>(std::forward<Tuple>(tuple))), void(), int{})...};
}

template<typename Tuple, typename F>
void for_each(Tuple &&tuple, F &&f) {
    constexpr std::size_t N = std::tuple_size<std::remove_reference_t<Tuple>>::value;

    for_each_impl(
            std::forward<Tuple>(tuple),
            std::forward<F>(f),
            std::make_index_sequence<N>{}
    );
}

double sum(double a) {
    return a;
}

double sum(int a) {
    return a;
}

template<typename T>
double sum(T a) {
    return 0;
}

template<typename... Ts>
double tuple_sum(const std::tuple<Ts...> &tpl) {
    double s = 0;
    for_each(tpl, [&](auto f) { s += sum(f); });
    return s;
}