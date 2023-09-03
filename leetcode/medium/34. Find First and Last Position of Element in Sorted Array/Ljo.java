package leetcode.easy;

public class Ljo {

    public int[] searchRange(int[] nums, int target) {
        int start = getIdx(nums, target, true);
        int end = getIdx(nums, target, false);
        return new int[] {start, end};
    }


    private int getIdx(int[] nums, int target, boolean isStart) {
        int left = 0;
        int right = nums.length - 1;
        int idx = -1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                if (isStart) {
                    idx = mid;
                    right = mid - 1;
                } else {
                    idx = mid;
                    left = mid + 1;
                }

            } else if (nums[mid] >= target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return idx;
    }

}
