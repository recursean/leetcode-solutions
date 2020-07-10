class Pr28 {
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }

    public static void main(String[] args) {
        String haystack = "hello";
        String needle = "ll";

        System.out.println(new Pr28().strStr(haystack, needle));
    }
}