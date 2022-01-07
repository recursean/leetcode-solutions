import java.util.regex.Pattern; 

class Pr1271 {
    public static void print(String s) { System.out.println(s); }

    public String toHexspeak(String num) {
        String hexStr = Long.toHexString(Long.parseLong(num));
        hexStr = hexStr.replace("0", "O");
        hexStr = hexStr.replace("1", "I");
        hexStr = hexStr.toUpperCase();
        
        if(Pattern.matches(".*[^ABCDEFIO].*", hexStr)) {
            return "ERROR";
        }

        else {
            return hexStr;
        }
    }

    public static void main(String args[]) {
        print(new Pr1271().toHexspeak("747823223228"));
    }
}