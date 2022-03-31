#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:    
    def romanToInt(self, s: str) -> int:
        tot = 0
        index = 0
        symbols = list(s)
        end = len(symbols) - 1

        while index <= end:
            curr = getRomanToInt(symbols[index])

            if index == end:
                nxt = 0
            else:
                nxt = getRomanToInt(symbols[index + 1])

            if curr < nxt:
                tot = tot + (nxt - curr)
                index = index + 2
            else:
                tot = tot + curr
                index = index + 1
        
        return tot

def getRomanToInt(roman: str) -> int:
    if roman == 'I':
        return 1
    elif roman == 'V':
        return 5
    elif roman == 'X':
        return 10
    elif roman == 'L':
        return 50
    elif roman == 'C':
        return 100
    elif roman == 'D':
        return 500
    elif roman == 'M':
        return 1000    

# @lc code=end