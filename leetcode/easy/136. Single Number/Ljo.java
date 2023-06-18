package leetcode.easy;

import java.util.ArrayList;
import java.util.HashSet;

public class Ljo {
    public int singleNumber(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int num: nums) {
            if(set.contains(num)) {
                set.remove(num);
            } else {
                set.add(num);
            }
        }
        return new ArrayList<>(set).get(0);
    }

    // bit 연산자 이용
//    public int singleNumber(int[] nums) {
//        int ans = nums[0];
//
//        for(int i = 1 ; i < nums.length ; i++){
//            ans = ans ^ nums[i];
//        }
//
//        return ans;
//    }
}
