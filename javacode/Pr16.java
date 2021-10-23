class Pr16 {
    public int threeSumClosest(int[] nums, int target) {
        int close = 1001;
        for(int i = 0; i < nums.length - 2; i++) {
            for(int j = i+1; j < nums.length - 1; j++) {
                for(int k = j+1; k < nums.length; k++) {
                  close = Math.abs(target - (nums[i] + nums[j] + nums[k])) < Math.abs(target - close) ? 
                      (nums[i] + nums[j] + nums[k]) : close;
                }
            }
        }
        
        return close;
    }
}
