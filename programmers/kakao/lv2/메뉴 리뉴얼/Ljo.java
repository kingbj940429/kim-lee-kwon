package 프로그래머스.kakao.lv2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

// 메뉴 리뉴얼, https://school.programmers.co.kr/learn/courses/30/lessons/72411?language=java
public class Ljo {

    public static String[] solution(String[] orders, int[] course) {
        ArrayList<String> answer = new ArrayList<>();
        for (int value : course) {
            HashMap<String, Integer> map = new HashMap<>();
            for (String order : orders) {
                if (order.length() < value) {
                    continue;
                }
                char[] arr = order.toCharArray();
                Arrays.sort(arr);
                combination(arr, new boolean[arr.length], 0, value, map);
            }
            answer.addAll(resolveResult(map));
        }
        Collections.sort(answer);
        return answer.toArray(new String[0]);
    }

    private static List<String> resolveResult(HashMap<String, Integer> map) {
        ArrayList<String> result = new ArrayList<>();
        int maxValue = 2;
        for (Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() >= maxValue) {
                if (entry.getValue() != maxValue) {
                    result.clear();
                    maxValue = entry.getValue();
                }
                result.add(entry.getKey());

            }
        }
        return result;
    }

    private static void combination(char[] arr, boolean[] visited, int start, int r, HashMap<String, Integer> map) {
        if (r == 0) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < visited.length; i++) {
                if (visited[i]) {
                    sb.append(arr[i]);
                }
            }
            String res = sb.toString();
            map.put(res, map.containsKey(res) ? map.get(res) + 1 : 1);
            return;
        }
        for (int i = start; i < arr.length; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, r - 1, map);
            visited[i] = false;
        }
    }

}
