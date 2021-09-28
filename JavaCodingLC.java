/* LC922: Sort Array by Parity in-place */
class Solution922 {
    public int[] sortArrayByParityII(int[] nums) {
        int i = 0, j = 1;
        while (i < nums.length) {
            // odd + even = odd
            if ((i + nums[i]) % 2 != 0) {
                while (j < nums.length && (j + nums[j]) % 2 == 0) {
                    j += 2;
                }
                if (j < nums.length) {
                    int temp = nums[j];
                    nums[j] = nums[i];
                    nums[i] = temp;
                }
            }
            i += 2;
        }
        return nums;
    }
}
