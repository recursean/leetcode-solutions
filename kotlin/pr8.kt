fun myAtoi(str: String): Int {
    var tstr = str.trim(' ')
    
    if(tstr == "" || (!tstr.get(0).isDigit() && tstr.get(0) != '-' && tstr.get(0) != '+')) {
        return 0
    }
    
    else {
        var idx = tstr.length
        
        for(i in 0 until tstr.length) {
            if(!tstr.get(i).isDigit() && i != 0) {
                idx = i 
                break
            }
        }
        
        try {
            return tstr.substring(0..idx-1).toInt()
        }

        catch(e: NumberFormatException) {
            if(tstr.length == 1 || !tstr.get(1).isDigit()) {
                return 0 
            }

            else {
                if(tstr.get(0) == '-') {
                    return Int.MIN_VALUE
                }

                else {
                    return Int.MAX_VALUE
                }
            }
        }
    }
}

fun main() {
    print(myAtoi("+-2"))
}