package javacode;

public class Pr26 {
    public int removeDuplicates(int[] nums) {
        int currNum = 0;
        int pivot = -1;
        int prevPivotVal = -1;
        int dups = 0;

        for(int i = 0; i < nums.length; i++) {
            if(i == 0) {
                currNum = nums[i];
            }

            else if(currNum == nums[i]) {
                if(pivot == -1) {
                    pivot = i;
                }

                dups++;
            }

            else {
                currNum = nums[i];

                if(pivot != -1) {
                    // save to compare to next number
                    prevPivotVal = nums[pivot];

                    // swap the unique number with current pivot
                    nums[pivot] = currNum; 

                    // make pivot+1 the new pivot
                    pivot++;
                }
            }
        }

        return nums.length - dups;
    }


    public static void main(String[] args) {
        int[] nums = {0,0,1,1,1,2,2,3,3,4};
        System.out.println(new Pr26().removeDuplicates(nums));
    }
}