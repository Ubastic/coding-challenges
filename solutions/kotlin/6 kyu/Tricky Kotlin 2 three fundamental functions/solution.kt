fun unless(value: Boolean, block: () -> Unit) = if (!value) block() else null

fun until(predicate: () -> Boolean, block: () -> Unit) {
    while (!predicate()) block()
}

fun forceRun(block: () -> Unit) {
    try {
        block()
    } catch (e: Exception) {
    }
}