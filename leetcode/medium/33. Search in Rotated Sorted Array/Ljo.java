package leetcode.easy;

public class Ljo {

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int idx = -1;
        while (left <= right) {
            int mid = (left + right) / 2;
            int value = nums[mid];
            if (value == target) {
                return mid;
            }
            if (nums[left] <= nums[mid]) { // start ~ mid 부분배열이 오름차순
                if (nums[left] <= target && target <= nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else { // mid ~ end 부분배열이 오름차순
                if (nums[mid] <= target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }

        }
        return idx;
    }

}
