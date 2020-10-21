public class Pr1512 {
    public int numIdenticalPairs(int[] nums) {
        int pairs = 0;

        for(int i = 0; i < nums.length - 1; i++) {
            for(int j = i + 1; j < nums.length; j++) {
                if(nums[i] == nums[j]) {
                    pairs++;
                }
            }
        }

        return pairs;
    }
    
    public static void main(String[] args) {
        int[] nums = {1,2,3,1,1,3};

        System.out.println(new Pr1512().numIdenticalPairs(nums));
    }
}