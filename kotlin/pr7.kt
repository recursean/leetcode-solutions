fun reverse(x: Int): Int {
    var str = "$x"
    var rev = str.reversed()

    if(rev.substring(rev.length - 1..rev.length - 1) == "-") {   
        rev = "-${rev.substring(0..rev.length - 2)}"
    }

    try {
        return rev.toInt()
    }

    catch(e: NumberFormatException) {
        return 0
    }
}

fun main() {
    print(reverse(-2147483648))
}