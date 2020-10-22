// Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Pr1281 {
    public int subtractProductAndSum(int n) {
        int sum = 0;
        int product = 0;
        boolean prodInit = false;

        for(int i = (new Integer(n)).toString().length(); i > 0; i--) {
            int dec = (int)Math.pow(10, i-1);
            int num = n / dec;

            sum += num;

            if(prodInit == false) {
                prodInit = true;
                product = num;
            }
            else {
                product *= num;
            }

            n -= num * dec;
        }

        return product - sum; 
    }

    public static void main(String[] args) {
        int n = 234;
        System.out.println(new Pr1281().subtractProductAndSum(n));
    }
}