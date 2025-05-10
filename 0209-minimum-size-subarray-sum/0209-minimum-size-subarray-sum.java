class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0,right = 0,sum = 0,len = Integer.MAX_VALUE;
        for(right = 0;right < nums.length;right++){
            sum += nums[right];
            while (sum >= target){
                if((right - left + 1) < len){
                    len = right - left + 1;
                }
                sum -= nums[left];
                left++;
            }
        }
        return len != Integer.MAX_VALUE ? len : 0;
    }
}