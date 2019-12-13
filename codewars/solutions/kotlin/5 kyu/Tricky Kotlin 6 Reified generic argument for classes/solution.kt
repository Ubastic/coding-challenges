class TrickyKotlin6<T>(val type: Class<T>) {
    inline fun <reified R> classOrSuperClassOf(a: () -> R) = type.isAssignableFrom(R::class.java)
}

inline fun <reified T> TrickyKotlin6() = TrickyKotlin6(T::class.java)
