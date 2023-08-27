package leetcode.easy;

import java.util.Arrays;

public class Ljo {
    
    public void nextPermutation(int[] nums) {
        int idx = -1;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                idx = i;
                break;
            }
        }
        if (idx == -1) { // reverse, in place
            reverse(nums, 0, nums.length - 1);
        } else {
            int greaterIdx = -1;
            for (int i = nums.length - 1; i >= 0; i--) {
                if (nums[i] > nums[idx]) {
                    greaterIdx = i;
                    break;
                }
            }
            swap(nums, idx, greaterIdx);
            reverse(nums, idx + 1, nums.length - 1);
        }

    }

    private void swap(int[] nums, int idx, int idx2) {
        int temp = nums[idx];
        nums[idx] = nums[idx2];
        nums[idx2] = temp;
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }

}
