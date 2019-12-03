class Pr4 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int idx1 = 0;
        int idx2 = 0;

        int[] sorted = new int[(nums1.length + nums2.length) / 2 + 1];

        for(int i = 0; i < (nums1.length + nums2.length) / 2 + 1; i++) {
            if(idx1 < nums1.length && idx2 < nums2.length) {
                if(nums1[idx1] <= nums2[idx2]) {
                    sorted[i] = nums1[idx1++];
                }
    
                else {
                    sorted[i] = nums2[idx2++];
                }
            }

            else {
                if(idx1 == nums1.length) {
                    sorted[i] = nums2[idx2++];
                }

                else {
                    sorted[i] = nums1[idx1++];
                }
            }
        }

        if((nums1.length + nums2.length) % 2 == 0) {
            return (sorted[sorted.length - 1] + sorted[sorted.length - 2]) / 2.0;
        }

        else {
            return sorted[sorted.length - 1];
        }
    }

    public static void main(String[] args) {
        int[] nums1 = {1, 3};
        int[] nums2 = {2, 4};

        System.out.println(new Pr4().findMedianSortedArrays(nums1, nums2));
    }
}