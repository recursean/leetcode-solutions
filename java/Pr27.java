class Pr27 {
    public void swap(int[] nums, int a, int b) {
        int t = nums[a];
        nums[a] = nums[b];
        nums[b] = t;
    }

    public int removeElement(int[] nums, int val) {
        int ctr = 0;
        int offset = 1;

        if(nums.length == 0) {
            return nums.length;
        }
        else if(nums.length == 1) {
            if(nums[0] == val) {
                return 0;
            }
            else {
                return nums.length;
            }
        }

        for(int i = 0; i < nums.length - offset; i++) {
            if(nums[i] == val) {
                ctr++;

                while(nums[nums.length - offset] == val) {
                    ctr++;
      
                    if(i >= nums.length - ++offset) {
                        break;
                    }
                }

                swap(nums, i, nums.length - offset++);
            }
        }

        if(offset < nums.length && nums[nums.length - offset] == val) {
            ctr++;
        }

        return nums.length - ctr;
    }

    public static void main(String[] args) {
        int nums[] = {3,3};
        int val = 3;
        System.out.println(new Pr27().removeElement(nums, val));
    }
}