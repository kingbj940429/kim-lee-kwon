package 프로그래머스.kakao.lv2;

import java.util.*;

// 오픈채팅방, https://school.programmers.co.kr/learn/courses/30/lessons/42888
class Ljo {
    static Map<String, String> userMap = new HashMap<>();

    public String[] solution(String[] record) {
        int size = record.length;
        StringTokenizer st;
        for(String msg: record) {
            st = new StringTokenizer(msg);
            String command = st.nextToken();
            String userId = st.nextToken();
            if (command.equals("Change")) {
                size--;
            }
            if(st.hasMoreTokens()) {
                userMap.put(userId, st.nextToken());
            }

        }
        int idx = 0;
        String[] answer = new String[size];
        for(String msg: record) {
            st = new StringTokenizer(msg, " ");
            String command = st.nextToken();
            String userId = st.nextToken();
            if(!command.equals("Change")) {
                answer[idx++] = translateCommand(command, userId);
            }
        }
        return answer;
    }
    public String translateCommand(String command, String userId) {
        StringBuilder sb = new StringBuilder(userMap.get(userId));
        if(command.equals("Enter")) {
            sb.append("님이 들어왔습니다.");
        } else {
            sb.append("님이 나갔습니다.");
        }
        return sb.toString();
    }
}
