package leetcode.easy;

public class Ljo {


    public int jump(int[] nums) {
        int jumps = 0;
        int curEnd = 0;
        int curFarthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            curFarthest = Math.max(curFarthest, i + nums[i]);
            if (i == curEnd) {
                jumps++;
                curEnd = curFarthest;
            }
        }
        return jumps;
    }

//    public int jump(int[] nums) {
//        int[] answer = new int[] {
//            Integer.MAX_VALUE
//        };
//        search(nums, 0, 0, answer);
//        return answer[0];
//    }
//
//    private void search(int[] nums, int currentIdx, int count, int[] answer) {
//        if (count >= answer[0] || currentIdx > nums.length - 1) {
//            return;
//        }
//        if (currentIdx == nums.length - 1) {
//            answer[0] = count;
//        }
//        for (int i = 1; i <= nums[currentIdx]; i++) {
//            search(nums, currentIdx + i, count + 1, answer);
//        }
//    }

}
