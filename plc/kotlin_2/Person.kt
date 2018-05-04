data class Person(var name: String? = null,
                  var age: Int? = null,
                  var address: Address? = null)

data class Address(var street: String? = null,
                   var number: Int? = null,
                   var city: String? = null)

fun main(args: Array<String>) {
    val john = person {
        name = "John"
        age = 25
        address {
            street = "Main Street"
            number = 42
            city = "London"
        }
    }
    println(john)
}

fun person(lambda: Person.() -> Unit) : Person = Person().apply(lambda)

fun Person.address(lambda: Address.() -> Unit) {
    val a = Address()
    a.lambda()
    this.address = a
}

