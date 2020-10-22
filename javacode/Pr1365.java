// Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
// That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

public class Pr1365 {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] results = new int[nums.length];

        for(int i = 0; i < nums.length; i++) {
            for(int j = i + 1; j < nums.length; j++) {
                if(nums[i] > nums[j]) {
                    results[i]++;
                }
                else if(nums[i] < nums[j]){
                    results[j]++;
                }
            }
        }

        return results;
    }

    public static void main(String[] args) {
        int[] nums = {8,1,2,2,3};
        int[] results = new Pr1365().smallerNumbersThanCurrent(nums);
        for(int result: results) {
            System.out.println(result);
        }
    }
}