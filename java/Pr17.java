import java.util.ArrayList;
import java.util.List;

class Pr17 {
    public int plen(String s) {
        int len = 1;

        for(int i = 0; i < s.length(); i++) {
            len *= letters(s.charAt(i)).length;
        }

        return len;
    } 

    public char[] letters(char c) {
        switch(c) {
            case '2':
                return "abc".toCharArray();
            case '3':
                return "def".toCharArray();
            case '4':
                return "ghi".toCharArray();
            case '5':
                return "jkl".toCharArray();
            case '6':
                return "mno".toCharArray();
            case '7':
                return "pqrs".toCharArray();
            case '8':
                return "tuv".toCharArray();
            case '9':
                return "wxyz".toCharArray();           
        }

        return "".toCharArray();
    }

    public List<String> letterCombinations(String digits) {
        List<String> ans = new ArrayList<String>();

        if(digits.length() == 0) {
            return ans;
        }
        else if(digits.length() == 1) {
            for(char c: letters(digits.charAt(0))) {
                ans.add(String.valueOf(c));
            }
        }
        else {
            // init
            for(char c: letters(digits.charAt(0))) {
                for(int i = 0; i < plen(digits.substring(1, digits.length())); i++) {
                    ans.add(String.valueOf(c));
                }
            }
      
            // rest
            for(int i = 1; i < digits.length(); i++) {
                int n = plen(digits.substring(i));

                int l = 1;
                if(i + 1 < digits.length()) {
                    l = plen(digits.substring(i + 1));
                }

                char[] letters = letters(digits.charAt(i));

                for(int j = 0; j < plen(digits); j += n) {
                    int start  = 0;

                    for(char c: letters) {
                        for(int k = start; k < start + l; k++) {
                            ans.set(j + k, ans.get(j + k) + String.valueOf(c));
                        }

                        start += l;
                    }
                }
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        List<String> ans = new Pr17().letterCombinations("237");
        for(String s: ans) {
            System.out.println(s);
        }
    }
}