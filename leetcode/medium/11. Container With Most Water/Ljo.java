package leetcode.easy;

public class Ljo {

    public int maxArea(int[] height) {
        int max = 0;
        int left = 0;
        int right = height.length - 1;
        while (left < right) {
            max = Math.max(max, calculateArea(height, left, right));
            if (height[left] <= height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return max;
    }

    private int calculateArea(int[] height, int left, int right) {
        int width = right - left;
        int minHeight = Math.min(height[left], height[right]);
        return width * minHeight;
    }

}
