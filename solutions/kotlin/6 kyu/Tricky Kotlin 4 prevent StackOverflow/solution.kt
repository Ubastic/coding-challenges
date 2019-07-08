import java.util.*

fun loop(random: Random, int: Int): Int = (0..int + 1).reduce { _, _ -> random.nextInt() }
