class Solution {
    fun numJewelsInStones(J: String, S: String): Int {
        var ctr = 0
        
        for(i in 0 until S.length) {
            if(J.contains(S.get(i))) {
                ctr++
            }   
        }
        
        return ctr
    }
}
