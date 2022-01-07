// A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

// We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

// The rules of Goat Latin are as follows:

// If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
// For example, the word 'apple' becomes 'applema'.
 
// If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
// For example, the word "goat" becomes "oatgma".
 
// Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
// For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
// Return the final sentence representing the conversion from S to Goat Latin. 

class Pr824 {
    public String toGoatLatin(String S) {
        String[] words = S.split(" ");
        String addOn = "a";
        String returnStr = "";
        String ma = "ma";

        for(int i = 0; i < words.length; i++) {
            if( words[i].toLowerCase().charAt(0) == 'a' || 
                words[i].toLowerCase().charAt(0) == 'e' || 
                words[i].toLowerCase().charAt(0) == 'i' || 
                words[i].toLowerCase().charAt(0) == 'o' || 
                words[i].toLowerCase().charAt(0) == 'u') {
                    words[i] = words[i] + ma + addOn;
            }

            else {
                words[i] = words[i].substring(1, words[i].length()) + Character.toString(words[i].charAt(0)) + ma + addOn;
            }

            addOn += "a";

            returnStr += " " + words[i];
        }

        return returnStr.substring(1, returnStr.length());
    }

    public static void main(String[] args) {
        System.out.println(new Pr824().toGoatLatin("I speak Goat Latin"));
    }
}