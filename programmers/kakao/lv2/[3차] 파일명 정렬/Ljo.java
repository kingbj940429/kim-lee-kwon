import java.util.*;


class Ljo {

    static class File implements Comparable<File> {

        int idx;
        String fullName;
        String head;
        int number;

        public File(int idx, String fullName, String head, int number) {
            this.idx = idx;
            this.fullName = fullName;
            this.head = head;
            this.number = number;
        }

        @Override
        public int compareTo(File o) {
            int headResult = this.head.compareToIgnoreCase(o.head);
            if (headResult != 0) {
                return headResult;
            }
            int numberResult = Integer.compare(this.number, o.number);
            if (numberResult != 0) {
                return numberResult;
            }
            return Integer.compare(this.idx, o.idx);
        }


    }

    public String[] solution(String[] files) {

        File[] fileArr = new File[files.length];
        for (int i = 0; i < files.length; i++) {
            String[] result = splitFileName(files[i]);
            fileArr[i] = new File(i, files[i], result[0], Integer.parseInt(result[1]));
        }
        Arrays.sort(fileArr);

        String[] answer = new String[fileArr.length];
        for(int i=0; i<fileArr.length; i++) {
            answer[i] = fileArr[i].fullName;
        }
        return answer;
    }

    private static String[] splitFileName(String file) {
        char[] charArray = file.toCharArray();
        int start = -1;
        int end = -1;
        int size = 0;

        boolean flag = true;
        for (int i = 0; i < charArray.length; i++) {
            char ch = charArray[i];
            if (Character.isDigit(ch)) {
                if (flag) {
                    start = i;
                    flag = false;
                }
                size++;
            } else if (!flag) {
                break;
            }
        }

        end = start + size - 1;
        return new String[] {file.substring(0, start), file.substring(start, end + 1)};

    }
}
