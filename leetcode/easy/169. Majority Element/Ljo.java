package leetcode.easy;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Ljo {

    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }
        Entry<Integer, Integer> max = map.entrySet()
            .stream()
            .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
            .findFirst()
            .get();
        return max.getKey();
    }

    // https://sgc109.github.io/2020/11/30/boyer-moore-majority-vote-algorithm/
//    public int majorityElement(int[] nums) {
//        int count = 0, maxElement = 0;
//        for(int num: nums) {
//            if(count == 0) {
//                maxElement = num;
//            }
//            if(num == maxElement) {
//                count++;
//            } else {
//                count--;
//            }
//        }
//
//        return maxElement;
//    }

}
