class Solution {
    fun convert(s: String, numRows: Int): String {
        var output = ""
        
        if(numRows == 1) {
            output = s
        }
        
        else {
            var idx = 0
            var ctr = 0
            
            for(i in 0 until numRows) {
                idx = i
                
                while(idx < s.length) {
                    output += s.substring(idx..idx)
                    
                    if(i == numRows - 1) {
                        idx += numRows + (numRows - 2) 
                    }
                    
                    else if(ctr % 2 == 0 || i == 0) {
                        idx += numRows + (numRows - 2 * (i + 1))    
                    }
                    
                    else {
                        idx += 2 * i  
                    }
                    
                    ctr++
                }       
                
                ctr = 0
            }
        }
        
        return output
    }
}
