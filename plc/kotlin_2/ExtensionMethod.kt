package dsl.ex03
fun String?.IsNullOrSingleLetter(): String {
    if (this == null || this.length == 1) {
        return "true"
    } else {
        return "false"
    }
}

fun main(args: Array<String>) {
    val line : String? = null
     println(line.IsNullOrSingleLetter())
     println("A".IsNullOrSingleLetter())
     println("Hello, world".IsNullOrSingleLetter())
}