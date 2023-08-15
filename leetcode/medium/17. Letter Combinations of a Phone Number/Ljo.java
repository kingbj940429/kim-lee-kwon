package leetcode.easy;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Ljo {

    public List<String> letterCombinations(String digits) {
        var letterByDigit = Map.of(
            '2', "abc",
            '3', "def",
            '4', "ghi",
            '5', "jkl",
            '6', "mno",
            '7', "pqrs",
            '8', "tuv",
            '9', "wxyz"
        );
        var answer = new ArrayList<String>();
        if (digits.length() > 0) {
            combination(answer, 0, letterByDigit, digits.toCharArray(), new StringBuilder());
        }
        return answer;
    }

    private void combination(List<String> answer, int start, Map<Character, String> letterByDigit, char[] digitArr,
        StringBuilder sb) {
        if (sb.length() == digitArr.length) {
            answer.add(sb.toString());
            return;
        }

        var charArr = letterByDigit.get(digitArr[start]).toCharArray();
        for (char c : charArr) {
            sb.append(c);
            combination(answer, start + 1, letterByDigit, digitArr, sb);
            sb.deleteCharAt(sb.length() - 1);
        }
    }


}
