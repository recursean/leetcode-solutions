public class Pr1342 {
    public int numberOfSteps(int num) {
        int numc = num;
        int steps = 0;
        
        while(numc != 0) {
            if(numc % 2 == 0) {
                numc /= 2;
            }
            else {
                numc -= 1;
            }

            steps++;
        }

        return steps;
    }

    public static void main(String[] args) {
        int num = 14;

        System.out.println(new Pr1342().numberOfSteps(num));
    }
}