template <int x>
struct factorial { 
    enum: long long { value = x * factorial<x-1>::value };
};

template <>
struct factorial<0> {
  enum: long long { value = 1 };
};