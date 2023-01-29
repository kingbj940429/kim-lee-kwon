package 프로그래머스.kakao;

import java.util.*;

public class Ljo {

    static class Tuple {

        int x;
        int y;

        Tuple(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public String solution(int[] numbers, String hand) {
        final int START = 10;
        final int SHARP = 11;
        StringBuilder sb = new StringBuilder();
        Map<Integer, Tuple> numberPosition = new HashMap<>();
        // *, START
        numberPosition.put(START, new Tuple(3, 0));
        // 0
        numberPosition.put(0, new Tuple(3, 1));
        // #, SHARP
        numberPosition.put(SHARP, new Tuple(3, 2));
        for (int i = 1; i < 10; i++) {
            numberPosition.put(i, new Tuple((i - 1) / 3, (i - 1) % 3));
        }
        int leftPrev = START;
        int rightPrev = SHARP;
        int leftDist;
        int rightDist;
        for (int number : numbers) {
            if (number == 1 || number == 4 || number == 7) {
                sb.append("L");
                leftPrev = number;
            } else if (number == 3 || number == 6 || number == 9) {
                sb.append("R");
                rightPrev = number;
            } else {
                Tuple pos = numberPosition.get(number);
                Tuple leftPos = numberPosition.get(leftPrev);
                Tuple rightPos = numberPosition.get(rightPrev);
                leftDist = Math.abs(pos.x - leftPos.x) + Math.abs(pos.y - leftPos.y);
                rightDist = Math.abs(pos.x - rightPos.x) + Math.abs(pos.y - rightPos.y);

                if (leftDist > rightDist) {
                    sb.append("R");
                    rightPrev = number;

                } else if (leftDist < rightDist) {
                    sb.append("L");
                    leftPrev = number;
                } else {
                    if (hand.equals("left")) {
                        sb.append("L");
                        leftPrev = number;
                    } else {
                        sb.append("R");
                        rightPrev = number;
                    }

                }

            }
        }
        return sb.toString();
    }

}
