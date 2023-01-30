package 프로그래머스.kakao;

// 비밀지도, https://school.programmers.co.kr/learn/courses/30/lessons/17681
public class Ljo {
    

    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for (int i = 0; i < n; i++) {
            int value = arr1[i] | arr2[i];
            answer[i] = String.format("%" + n + "s", Integer.toBinaryString(value))
                .replace(' ', '0')
                .replace("1", "#")
                .replace("0", " ");
        }
        return answer;
    }

}
