class Pr14 {
    public String longestCommonPrefix(String[] strs) {
        String sub = "";
        byte idx = 0;

        for(String str: strs) {
            if(sub == "") {
                sub = str;
            }
            
            else {
                for(int i = 0; i < str.length() && i < sub.length(); i++) {
                    if(sub.charAt(i) != str.charAt(i)) {
                        break;
                    }
                    else {
                        idx++;
                    }
                }

                sub = sub.substring(0, idx);

                if(sub == "") {
                    break;
                }

                idx = 0;
            }
        }
        
        return sub;
    }
    
    public static void main(String[] args) {
        String[] strs = {"flower","flow","flight"};
        System.out.println(new Pr14().longestCommonPrefix(strs));
    }
}