package leetcode.easy;

import java.util.ArrayList;
import java.util.List;

public class Ljo {

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        permute(nums, nums.length, result, new boolean[nums.length], new ArrayList<>());
        return result;
    }

    private void permute(int[] nums, int depth, List<List<Integer>> result, boolean[] visited, List<Integer> temp) {
        if (depth == 0) {
            result.add(new ArrayList<>(temp));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                temp.add(nums[i]);
                permute(nums, depth - 1, result, visited, temp);
                temp.remove(temp.size() - 1);
                visited[i] = false;
            }
        }

    }


}
