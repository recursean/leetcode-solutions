public class Pr1480 {
    public int[] runningSum(int[] nums) {
        int[] sums = new int[nums.length];

        for(int i = 0; i < nums.length; i++) {
            if(i == 0) {
                sums[i] = nums[i];
            }
            else {
                sums[i] = sums[i-1] + nums[i];
            }
        }

        return sums;
    }
    
    public static void main(String[] args) {
        int[] nums = {1,2,3,4};
        int[] runningSum = new Pr1480().runningSum(nums);

        for(int sum: runningSum) {
            System.out.println(sum);
        }
    }
}