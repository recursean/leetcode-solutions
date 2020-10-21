public class Pr1528 {
    public String restoreString(String s, int[] indices) {
        char[] chars = new char[s.length()];

        for(int i = 0; i < indices.length; i++) {
            chars[indices[i]] = s.charAt(i);
        }

        return new String(chars);
    }
    
    public static void main(String[] args) {
        String s = "codeleet";
        int[] indices = {4,5,6,7,0,2,1,3};

        System.out.println(new Pr1528().restoreString(s, indices));
    }
}