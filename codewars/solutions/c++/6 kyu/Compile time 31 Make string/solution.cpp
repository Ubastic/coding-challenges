template <char... C>
struct make_string {
  constexpr static char value[sizeof...(C) + 1] = {C..., '\0'};
};

template <char... C>
constexpr char make_string<C...>::value[sizeof...(C) + 1];
