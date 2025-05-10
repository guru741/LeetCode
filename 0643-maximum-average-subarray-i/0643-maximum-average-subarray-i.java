class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int i = 0,j = 0,sum = 0;
        double max_sum = Double.NEGATIVE_INFINITY;
        while (j < nums.length){
            sum += nums[j];
            if ((j - i + 1) < k){
                j ++;
            }
            else if ((j - i + 1) == k){
                max_sum = Math.max(max_sum,sum);
                sum -= nums[i];
                i++;j++;
            }
        }
        return max_sum / k;
    }
}