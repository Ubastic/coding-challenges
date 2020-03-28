#include <cstddef>

template<typename T, typename... Ts>
constexpr std::size_t arg_length(T, Ts... xs) noexcept {
    int s = 1;
    for (auto &i : {xs...}) s++;

    return s;
}