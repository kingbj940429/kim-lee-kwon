package leetcode.easy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Ljo {

    public List<List<Integer>> threeSum(int[] nums) {
        int target = 0;
        Set<List<Integer>> hash = new HashSet<>();
        Arrays.sort(nums);
        for (int node = 0; node < nums.length; node++) {
            int left = node + 1;
            int right = nums.length - 1;
            while (left < right) {
                int sum = nums[node] + nums[left] + nums[right];
                if (sum == target) {
                    hash.add(Arrays.asList(nums[node], nums[left], nums[right]));
                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return new ArrayList<>(hash);
    }


}
