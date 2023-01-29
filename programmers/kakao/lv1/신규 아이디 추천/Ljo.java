package 프로그래머스.kakao;

// 신규 아이디 추천, https://school.programmers.co.kr/learn/courses/30/lessons/72410
public class Ljo {

    public static void main(String[] args) {
        solution("...!@BaT#*..y.abcdefghijklm");
        solution("z-+.^.");
        solution("=.=");
        solution("123_.def");
        solution("abcdefghijklmn.p");
    }

    public static String solution(String new_id) {
        String answer = "";
        answer = new_id.toLowerCase();
//        System.out.println("1: " + answer);
        answer = answer.replaceAll("[^0-9a-z-_.]", "");
//        System.out.println("2: " + answer);

        answer = answer.replaceAll("[.]+", ".");
//        System.out.println("3: " + answer);

        if (answer.length() > 0) {
            if (answer.charAt(0) == '.') {
                if (answer.length() == 1) {
                    answer = "";
                } else {
                    answer = answer.substring(1);
                }
            }
            if (answer.length() > 0 && answer.charAt(answer.length() - 1) == '.') {
                answer = answer.substring(0, answer.length() - 1);
            }
//            System.out.println("4: " + answer);
        }
        if (answer.equals("")) {
            answer = "a";
        }
//        System.out.println("5: " + answer);

        if (answer.length() >= 16) {
            answer = answer.substring(0, 15);
            if (answer.charAt(14) == '.') {
                answer = answer.substring(0, 14);
            }
        }
//        System.out.println("6: " + answer);

        if (answer.length() <= 2) {
            int diff = 3 - answer.length();
            answer += String.valueOf(answer.charAt(answer.length() - 1)).repeat(diff);

        }
//        System.out.println("7: " + answer);
        return answer;
    }

    // 남의꺼
    public String solution2(String new_id) {
        String answer = "";
        String temp = new_id.toLowerCase();

        temp = temp.replaceAll("[^-_.a-z0-9]", "");
        temp = temp.replaceAll("[.]{2,}", ".");
        temp = temp.replaceAll("^[.]|[.]$", "");
        if (temp.equals("")) {
            temp += "a";
        }
        if (temp.length() >= 16) {
            temp = temp.substring(0, 15);
            temp = temp.replaceAll("^[.]|[.]$", "");
        }
        if (temp.length() <= 2) {
            while (temp.length() < 3) {
                temp += temp.charAt(temp.length() - 1);
            }
        }

        answer = temp;
        return answer;
    }

}
