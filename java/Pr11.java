class Pr11 {
    public int maxArea(int[] height) {
        int max = 0;

        for(int i = 1; i <= height.length; i++) {
            for(int j = height.length; j > i; j--) {
                if(height[i-1] <= height[j-1]) {
                    if((j - i) * height[i-1] > max) {
                        max = (j - i) * height[i-1];
                    }
                }
                else if((j - i) * height[j-1] > max) {
                    max = (j - i) * height[j-1];
                }
            }
        }

        return max;
    }

    public static void main(String[] args) {
        int[] heights = {10,9,8,7,6,5,4,3,2,1};

        System.out.println(new Pr11().maxArea(heights));
    }
}