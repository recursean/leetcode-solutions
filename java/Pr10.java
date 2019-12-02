import java.util.regex.Pattern; 

class Pr10 {
    public boolean isMatch(String s, String p) {
        return Pattern.matches(p, s);
    }

    public static void main(String[] args) {
        System.out.println(new Pr10().isMatch("mississippi", "mis*is*p*."));
    }
}