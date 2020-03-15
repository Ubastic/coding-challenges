#define COMPARE(OP) \
friend MagicCompare<T> operator OP(MagicCompare<T> self, T other) { \
    return MagicCompare(other, self.previous && self.value OP other);\
}\
friend MagicCompare<T> operator OP(T other, MagicCompare<T> self) {\
    return MagicCompare(self.value, self.previous && other OP self.value);\
}\
friend MagicCompare<T> operator OP(MagicCompare<T> self, MagicCompare<T> other) {\
    return MagicCompare(other.value, self.previous && self.value OP other.value);\
}

#define ARITHMETIC(OP)\
friend MagicCompare<T> operator OP(T other, MagicCompare<T> self) {\
    return MagicCompare(other OP self.value, self.previous);\
}\
friend MagicCompare<T> operator OP(MagicCompare<T> self, T other) {\
    return MagicCompare(other OP self.value, self.previous);\
}\
friend MagicCompare<T> operator OP(MagicCompare<T> self, MagicCompare<T> other) {\
    return MagicCompare(other.value OP self.value, self.previous);\
}

#define ARITHMETIC_INPLACE(OP)\
void operator OP(T other) {\
    value OP other;\
}\
void operator OP(MagicCompare<T>& other) {\
    value OP other.value;\
}

#define UNARY(OP)\
MagicCompare<T> &operator OP() {\
    this->value OP;\
    return *this;\
}\

template<class T>
class MagicCompare {
private:
    T value;
    bool previous = true;
public:
    MagicCompare(T value, bool previous = true) : value(value), previous(previous) {}

    MagicCompare<T> &operator=(T other) {
        this->value = other;
        return *this;
    }

    explicit operator bool() {
        return this->previous;
    }

    operator T() {
        if (!previous)
            return MagicCompare(0);

        return this->value;
    }

    COMPARE(==)
    COMPARE(!=)
    COMPARE(<)
    COMPARE(<=)
    COMPARE(>)
    COMPARE(>=)

    ARITHMETIC(+)
    ARITHMETIC(-)
    ARITHMETIC(*)
    ARITHMETIC(/)

    ARITHMETIC_INPLACE(+=)
    ARITHMETIC_INPLACE(-=)
    ARITHMETIC_INPLACE(*=)
    ARITHMETIC_INPLACE(/=)

    UNARY(++)
    UNARY(--)
};