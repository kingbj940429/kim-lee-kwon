package 프로그래머스.kakao;

import java.util.Map;

public class Ljo {

    public int solution(String s) {
        StringBuilder sb = new StringBuilder();
        Map<String, String> nums = Map.of(
            "zero", "0",
            "one", "1",
            "two", "2",
            "three", "3",
            "four", "4",
            "five", "5",
            "six", "6",
            "seven", "7",
            "eight", "8",
            "nine", "9"
        );

        int left = 0;
        int right = 0;
        while (left < s.length()) {
            char ch = s.charAt(right);
            if (Character.isDigit(ch)) {
                sb.append(ch);
                right++;
                left = right;
            } else if (nums.containsKey(s.substring(left, right))) {
                sb.append(nums.get(s.substring(left, right)));
                right++;
                left = right;
            } else {
                right++;
            }
        }
        return Integer.parseInt(sb.toString());
    }

    // 풀이 이후
    public int solution2(String s) {
        String[] strArr = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for(int i = 0; i < strArr.length; i++) {
            s = s.replace(strArr[i], Integer.toString(i));
        }
        return Integer.parseInt(s);
    }

}
