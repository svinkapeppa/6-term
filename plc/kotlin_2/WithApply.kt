package dsl.ex05

fun <T> T.myApply(lambda : T.() -> Unit) : T{
    this.lambda()
    return this
}

fun <T> T.myWith(obj : T, lambda : T.() -> Unit) {
    obj.lambda()
}

fun main(args: Array<String>) {
    val map = mutableMapOf(1 to "one")
    map.apply { this[2] = "two"}
    with (map) { this[3] = "three" }
    println(map)
    
    // Есть стандартные функции apply и with. Нужно написать их реализации самостоятельно
}