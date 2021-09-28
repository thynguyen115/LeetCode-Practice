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

/* LC74: Search 2D MT */
class Solution74 {
    public boolean searchMatrix(int[][] matrix, int target) {
        // check each row, if the target is less than the first elem in the row
        // or bigger than the last elem of that row ==> stop that row
        // otherwise, do binary search
        int i = 0, row = matrix.length, col = matrix[0].length;
        while (i < row) {
            // start <= target <= end
            if (matrix[i][0] <= target && target <= matrix[i][col-1]) {
                // binary search
                int left = 0, right = col - 1;
                while (left < right) {
                    int mid = left + (right - left) / 2;
                    if (matrix[i][mid] == target) {
                        return true;
                    } else if (matrix[i][mid] > target) {
                        right = mid;
                    } else {
                        left = mid + 1;
                    }
                }
                
                if (matrix[i][left] == target) {
                    return true;
                }
            }
            i += 1;
        }
        return false;
    }
}
