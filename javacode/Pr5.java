class Pr5 {
    public Boolean isPalindrome(String s) {
        for(int i = 0; i < s.length() / 2; i++) {
            if(s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                return false;
            }    
        }
        
        return true;
    }

    public String longestPalindrome(String s) {
        String pal = "";
        String sub = "";

        for(int i = 0; i < s.length(); i++) {
            sub = s.substring(0, i + 1);

            if(isPalindrome(sub)) {
                pal = sub;
            }

            while(sub.length() > pal.length()) {
                sub = sub.substring(1);

                if(isPalindrome(sub)) {
                    pal = sub;
                }
            }
        }

        return pal;
    }

    public static void main(String[] args) {
        System.out.println(new Pr5().longestPalindrome("cbbd"));
    }
}