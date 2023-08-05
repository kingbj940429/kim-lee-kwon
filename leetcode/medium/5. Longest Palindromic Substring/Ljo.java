package leetcode.easy;

public class Ljo {

    public static void main(String[] args) {
        System.out.println(longestPalindrome2("cbbd"));
    }

    // 1000ms
    public String longestPalindrome(String s) {
        String max = "";
        for (int i = 0; i < s.length(); i++) {
            for (int j = s.length(); i < j; j--) {
                String str = s.substring(i, j);
                if (str.length() <= max.length()) {
                    continue;
                }
                var isPalindrome = isPalindrome(str);
                if (isPalindrome) {
                    max = str;
                }

            }
        }
        return max;

    }

    private boolean isPalindrome(String str) {
        for (int i = 0; i < str.length() / 2; i++) {
            char start = str.charAt(i);
            char end = str.charAt(str.length() - 1 - i);
            if (start != end) {
                return false;
            }
        }
        return true;
    }


    // 100 ms
    public static String longestPalindrome2(String s) {
        var charArr = s.toCharArray();
        // 가장 긴 문자열부터 팰린드롬 검사
        for (int length = s.length(); length > 1; length--) {
            for (int start = 0; start + length <= s.length(); start++) {
                boolean isPalindrome = true;
                // 처음부터 문자열 길이의 반틈만큼 문자가 같은지 비교
                for (int i = 0; i < length / 2; i++) {
                    if (charArr[start + i] != charArr[start + length - i - 1]) {
                        isPalindrome = false;
                        break;
                    }
                }

                if (isPalindrome) {
                    return s.substring(start, start + length);
                }
            }
        }
        return String.valueOf(s.charAt(0));
    }


}
