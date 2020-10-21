import java.util.ArrayList;
import java.util.List;

public class Pr1431 {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        ArrayList<Boolean> extras = new ArrayList<Boolean>(candies.length);
        
        // find max val
        int max = -1;
        for(int i = 0; i < candies.length; i++) {
            if(candies[i] > max) {
                max = candies[i];
            }
        }

        // determine if kids can have greatest candies
        for(int i = 0; i < candies.length; i++) {
            if(candies[i] + extraCandies >= max) {
                extras.add(new Boolean(true));
            }
            else {
                extras.add(new Boolean(false));
            }
        }

        return extras;
    }

    public static void main(String[] args) {
        int[] candies = {2,3,5,1,3};
        int extraCandies = 3;

        List<Boolean> extras = new Pr1431().kidsWithCandies(candies, extraCandies);

        for(boolean extra: extras) {
            System.out.println(extra);
        }
    }
}