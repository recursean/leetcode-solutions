class Solution {
    fun singleNumber(nums: IntArray): Int {
        var map = HashMap<Int, Int>(nums.size)
        var num = 0
        
        for(i in 0 until nums.size) {
            if(map.containsKey(nums[i])) {
                map.put(nums[i], 2)
            }
            else {
                map.put(nums[i], 1) 
            }
        }
        
        for(key in map.keys) {
            if(map.get(key) == 1) {
                num = key
                break
            }    
        }
        
        return num
    }
}
