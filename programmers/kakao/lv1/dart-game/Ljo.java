package 프로그래머스.kakao;

import java.util.ArrayList;
import java.util.Set;
import java.util.StringTokenizer;

// 다트게임, https://school.programmers.co.kr/learn/courses/30/lessons/17682
public class Solution4 {

    public static void main(String[] args) {
        solution("1D2S#10S");
    }

    public static int solution(String dartResult) {
        int answer = 0;
        int[] points = new int[3];

        int n = 0;
        int idx = 0;
        StringBuilder num = new StringBuilder();
        for (int i = 0; i < dartResult.length(); i++) {
            char ch = dartResult.charAt(i);

            if (Character.isDigit(ch)) {
                num.append(ch);

            }
            else if (ch == 'S' || ch == 'D' || ch == 'T') {
                n = Integer.parseInt(num.toString());
                if (ch == 'S') {
                    points[idx] = (int) Math.pow(n, 1);
                } else if (ch == 'D') {
                    points[idx] = (int) Math.pow(n, 2);
                } else {
                    points[idx] = (int) Math.pow(n, 3);
                }
                idx++;
                num = new StringBuilder();
            }
            else {
                if (ch == '*') {
                    points[idx - 1] *= 2;
                    if (idx - 2 >= 0) {
                        points[idx - 2] *= 2;
                    }
                } else {
                    points[idx - 1] *= (-1);
                }
            }
        }

        answer = points[0] + points[1] + points[2];
        return answer;
    }

}
