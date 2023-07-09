package leetcode.easy;

public class Ljo {

    public void moveZeroes(int[] nums) {

        int idx = 0;
        for (int num : nums) {
            if (num != 0) {
                nums[idx] = num;
                idx++;
            }
        }

        while (idx < nums.length) {
            nums[idx] = 0;
            idx++;
        }

    }

}

