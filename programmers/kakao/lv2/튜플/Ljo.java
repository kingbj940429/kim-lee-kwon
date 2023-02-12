package 프로그래머스.kakao.lv2;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;


class Ljo {

    public int[] solution(String s) {
        String[] strArr = s.replaceAll("[{}]", " ").trim().split(" ,");
        Arrays.sort(strArr, Comparator.comparing(String::length));
        int[] answer = new int[strArr.length];
        HashSet<Integer> set = new HashSet<>();
        int idx = 0;
        for (String str : strArr) {
            for (String st : str.split(",")) {
                int num = Integer.parseInt(st.trim());
                if (set.contains(num)) {
                    continue;
                }
                set.add(num);
                answer[idx++] = num;
            }
        }
        return answer;
    }
}
