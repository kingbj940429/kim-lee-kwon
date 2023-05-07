package leetcode.easy;

import java.util.*;

// two sum, https://leetcode.com/problems/two-sum/submissions/946009333/
class Ljo {

    public int[] twoSum(int[] nums, int target) {
        int[] answer = new int[2];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff)) {
                answer[0] = map.get(diff);
                answer[1] = i;
                break;
            }
            map.put(nums[i], i);
        }
        return answer;
    }
}
