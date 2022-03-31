#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = False
        n = x
        reminder = 0
        reverse = 0

        while n != 0:
            reminder = n % 10
            reverse = reverse * 10 + reminder
            n = int(n / 10)

        if x == reverse:
            flag = True

        return flag
        
# @lc code=end

