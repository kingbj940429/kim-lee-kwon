package 프로그래머스.kakao;

import java.util.ArrayList;
import java.util.StringJoiner;

// 실패율, https://school.programmers.co.kr/learn/courses/30/lessons/42889
public class Solution3 {

    public static void main(String[] args) {
        solution(5, new int[] {2, 1, 2, 6, 2, 4, 3, 3});
    }

    static class Rate {

        int num;
        double fail;

        public Rate(int num, double fail) {
            this.num = num;
            this.fail = fail;
        }

    }


    public static int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] total = new int[N + 1];
        int[] clear = new int[N + 1];
        for (int stage : stages) {
            boolean isEnd = stage == N + 1;
            int value = stage == N + 1 ? N : stage;
            if (!isEnd) {
                clear[stage]++;
            }
            for (int j = 1; j < value + 1; j++) {
                total[j]++;
            }
        }

        ArrayList<Rate> rates = new ArrayList<>();
        for (int i = 1; i < N + 1; i++) {
            double rate = clear[i] == 0 ? 0 : (double) clear[i] / total[i];
            rates.add(new Rate(i, rate));

        }
        rates.sort((o1, o2) -> Double.compare(o2.fail, o1.fail));
        for(int i=0; i<N; i++) {
            answer[i] = rates.get(i).num;
        }
        return answer;
    }

}
