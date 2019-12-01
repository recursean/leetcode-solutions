class Pr9 {
    public boolean isPalindrome(int x) {
        String xStr = Integer.valueOf(x).toString();

        for(int i = 0; i < xStr.length() / 2; i++) {
            if(xStr.charAt(i) != xStr.charAt(xStr.length() - 1 - i)) {
                return false;
            }    
        }
        
        return true;
    }

    public static void main(String args[]) {
        System.out.println(new Pr9().isPalindrome(123211));
    }
}