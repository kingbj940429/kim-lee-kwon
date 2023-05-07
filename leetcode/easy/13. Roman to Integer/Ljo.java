package leetcode.easy;

import java.util.*;

class Solution2 {
    public static final Map<Character, Integer> ROMAN = Map.of(
        'I', 1,
        'V', 5,
        'X', 10,
        'L', 50,
        'C', 100,
        'D', 500,
        'M', 1000
    );
    
    public int romanToInt(String s) {
        int prev = Integer.MAX_VALUE;
        int result = 0;
        for (char ch : s.toCharArray()) {
            int value = ROMAN.get(ch);
            if (value > prev) {
                result -= prev * 2;
            }
            result += value;
            prev = value;
        }
        return result;
    }

}
