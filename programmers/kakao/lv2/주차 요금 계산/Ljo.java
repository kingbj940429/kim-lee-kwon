package 프로그래머스.kakao.lv2;

import java.util.*;

class Ljo {

    public int[] solution(int[] fees, String[] records) {
        int[] answer;

        Map<String, String> map = new HashMap<>();
        Map<String, Integer> feeMap = new HashMap<>();

        for (String record : records) {
            feeMap.put(record.split(" ")[1], 0);
        }

        for (String record : records) {
            String[] infos = record.split(" ");

            if (map.containsKey(infos[1])) {
                String[] inTime = map.remove(infos[1]).split(":");
                String[] outTime = infos[0].split(":");

                int hour = Integer.parseInt(outTime[0]) - Integer.parseInt(inTime[0]);
                int minute = Integer.parseInt(outTime[1]) - Integer.parseInt(inTime[1]);

                feeMap.replace(infos[1], feeMap.get(infos[1]) + 60 * hour + minute);

            } else {
                map.put(infos[1], infos[0]); // 차 번호, 시간
            }
        }

        map.keySet().forEach(key -> {
            String[] inTime = map.get(key).split(":");
            int hour = 23 - Integer.parseInt(inTime[0]);
            int minute = 59 - Integer.parseInt(inTime[1]);
            feeMap.replace(key, feeMap.get(key) + 60 * hour + minute);
        });
        List<Map.Entry<String, Integer>> list = new ArrayList<>(feeMap.entrySet());
        list.sort(Comparator.comparingInt(o -> Integer.parseInt(o.getKey())));
        answer = new int[list.size()];

        for (int i = 0; i < answer.length; i++) {
            if (list.get(i).getValue() > fees[0]) {
                answer[i] = fees[1] + (int) Math.ceil((list.get(i).getValue() - fees[0]) / (double) fees[2]) * fees[3];
            } else {
                answer[i] = fees[1];
            }
        }
        return answer;
    }
}
