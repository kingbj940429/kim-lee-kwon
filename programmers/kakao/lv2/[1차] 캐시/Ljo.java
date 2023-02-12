package 프로그래머스.kakao.lv2;

import java.util.*;

public class Ljo {

    public static void main(String[] args) {
        System.out.println(solution(
            2, new String[] {"Jeju", "Pangyo", "NewYork", "newyork"}
        ));
    }

    public static int solution(int cacheSize, String[] cities) {
        int answer = 0;
        if (cacheSize == 0) {
            return 5 * cities.length;
        }
        Map<String, Integer> cache = new HashMap<>();
        for (int i = 0; i < cities.length; i++) {
            String city = cities[i].toLowerCase();
            if (cache.containsKey(city)) {
                answer++;
            } else {
                if (cache.size() == cacheSize) {
                    List<Map.Entry<String, Integer>> entryList = new LinkedList<>(cache.entrySet());
                    entryList.sort(Map.Entry.comparingByValue());
                    cache.remove(entryList.get(0).getKey());
                }
                answer += 5;
            }
            cache.put(city, i);
        }
        return answer;
    }


}
