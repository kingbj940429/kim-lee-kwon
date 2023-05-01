// k진수에서 소수 개수 구하기, https://school.programmers.co.kr/learn/courses/30/lessons/92335
public class Solution8 {

    public static void main(String[] args) {
        System.out.println(solution(437674, 3));
        System.out.println(solution(110011, 10));
        System.out.println(solution(213214213, 4));
        System.out.println(solution(11002111, 5));
        System.out.println(solution(11002111, 6));
        System.out.println(solution(11002111, 7));
        System.out.println(solution(11002111, 9));
        System.out.println(solution(11002111, 8));
    }

    public static int solution(int n, int k) {
        if (n == 1) {
            return 0;
        }
        int answer = 0;
        String str = Integer.toString(n, k);
        int startIdx = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '0') {
                if (startIdx == i) {
                    startIdx = i + 1;
                    continue;
                }
                long value = Long.parseLong(str.substring(startIdx, i));
                if (isPrime(value)) {
                    answer++;
                }
                startIdx = i + 1;
            }
        }
        if (startIdx < str.length()) {
            long value = Long.parseLong(str.substring(startIdx));
            if (isPrime(value)) {
                answer++;
            }
        }
        return answer;
    }


    private static boolean isPrime(long n) {
        if (n == 1) {
            return false;
        }
        for (int i = 2; i <= (int) Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

}
