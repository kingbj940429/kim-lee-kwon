package leetcode.easy;

import java.util.HashSet;
import java.util.Objects;

public class Ljo {
    
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }
        int maxLength = Integer.MIN_VALUE;
        var charSet = new HashSet<Character>();
        for (int i = 0; i < s.length(); i++) {
            charSet.add(s.charAt(i));
            for (int j = i + 1; j < s.length(); j++) {
                char ch = s.charAt(j);
                if (charSet.contains(ch)) {
                    break;
                } else {
                    charSet.add(ch);
                }
            }
            maxLength = Math.max(maxLength, charSet.size());
            charSet.clear();
        }
        return maxLength;
    }

}
