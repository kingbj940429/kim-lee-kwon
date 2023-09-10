package leetcode.easy;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Ljo {


    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Set<List<Integer>> answer = new HashSet<>();
        process(candidates, target, 0, answer, new int[candidates.length]);
        return new ArrayList<>(answer);
    }

    private void process(int[] candidates, int target, int sum, Set<List<Integer>> answer, int[] count) {
        if (sum > target) {
            return;
        }
        if (sum == target) {
            ArrayList<Integer> temp = new ArrayList<>();
            for (int i = 0; i < count.length; i++) {
                for (int j = 0; j < count[i]; j++) {
                    temp.add(candidates[i]);
                }
            }
            answer.add(temp);
        }
        for (int i = 0; i < candidates.length; i++) {
            count[i]++;
            sum += candidates[i];
            process(candidates, target, sum, answer, count);
            sum -= candidates[i];
            count[i]--;

        }
    }

}
