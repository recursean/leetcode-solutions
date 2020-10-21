public class Pr1470 {
    public int[] shuffle(int[] nums, int n) {
        int x = 0;
        int y = n;
        int idx = 0;

        int[] shuffled = new int[nums.length];
        while(x < n && idx < shuffled.length) {
            shuffled[idx++] = nums[x++];

            if(idx < shuffled.length) {
                shuffled[idx++] = nums[y++];
            }
        }

        return shuffled;
    }

    public static void main(String[] args) {
        int[] nums = {2,5,1,3,4,7};
        int n = 3;

        int[] shuffled = new Pr1470().shuffle(nums, n);

        for(int num: shuffled) {
            System.out.println(num);
        }
    }
}