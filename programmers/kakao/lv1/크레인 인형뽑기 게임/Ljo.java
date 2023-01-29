package 프로그래머스.kakao;

import java.util.ArrayDeque;
import java.util.Deque;

// 크레인 인형뽑기 게임, https://school.programmers.co.kr/learn/courses/30/lessons/64061
public class Ljo {

    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int[] lastPos = new int[board.length + 1];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int move : moves) {
            int now = getNowValue(board, lastPos, move - 1);
            if(now == 0) {
                continue;
            }
            if (!stack.isEmpty() && stack.peekLast() == now) {
                stack.pollLast();
                answer += 2;
                continue;
            }
            stack.add(now);
        }
        return answer;
    }

    private int getNowValue(int[][] board, int[] lastPos, int col) {
        for (int i = lastPos[col]; i < board.length; i++) {
            int value = board[i][col];
            if (value != 0) {
                board[i][col] = 0;
                lastPos[col] = i;
                return value;
            }
        }
        return 0;
    }

}
