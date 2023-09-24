package leetcode.easy;

import java.util.*;

public class Ljo {

    public static void main(String[] args) {
        groupAnagrams(new String[] {"ddddddddddg", "dgggggggggg"});
    }

    public static List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) {
            return new ArrayList<>();
        }
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String keyStr = String.valueOf(charArray);
            map.computeIfAbsent(keyStr, key -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(map.values());
    }

}
