/*
 * @lc app=leetcode id=1 lang=csharp
 *
 * [1] Two Sum
 */

// @lc code=start
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[] rst = new int[2];
        for (int i = 0; i < nums.Length; i++) {
            int first = nums[i];
            
            for (int j = i + 1; j < nums.Length; j++) {
                
                int second = nums[j];
                int sum = first + second;
                
                if (sum == target) {
                    rst[0] = i;
                    rst[1] = j;

                    return rst;
                }                
            }
        }
        
        return rst;
    }
}
// @lc code=end

