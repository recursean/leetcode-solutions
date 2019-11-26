class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        var long = 0
        var ctr = 0
        var visited = HashMap<Char, Int>(256)
        
        if(s.length == 1) {
            long = 1
        }
        
        else {
            for(i in 0 until s.length) {
                if(visited.containsKey(s.get(i))) {
                    var prev: Int = visited[s.get(i)]!!

                    if(i - ctr > prev) {
                        ctr++
                    }

                    else {
                        if(ctr > long) {
                            long = ctr
                        }

                        ctr = i - prev
                    }
                }

                else {
                    ctr++
                }

                visited.put(s.get(i), i)
            }   
            
            if(ctr > long) {
                long = ctr
            }
        }
        
        return long
    }
}
