package solution

import java.util.Optional

suspend fun <T> SequenceScope<Any>.bind(value: Optional<T>): T {
    yield(value)
    return value.get()
}

fun <T> `for`(block: suspend SequenceScope<Any>.() -> Unit): Optional<T> {
    sequence(block).forEach {
        when (it) {
            is Optional<*> -> if (!it.isPresent) return@`for` Optional.empty()
            else -> return@`for` Optional.of(it as T)
        }
    }
    return Optional.empty()
}