'''
Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.


Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:
-231 <= x <= 231 - 1
'''

# Answer

class Solution(object):
    def isPalindrome(self, x):
        if(x < 0):
            return False
        
        palindrome = 0
        num = x
        while(x != 0):
            palindrome = (palindrome * 10) + x % 10
            x = x // 10
        if(palindrome == num):
            return True
        return False
    

'''
Language: Python
Runtime: 47ms
Memory: 13.5 MB
Date: 11/08/2023
Hour: 11:24 AM
'''