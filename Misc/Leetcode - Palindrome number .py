# Determine whether an integer is a palindrome. Do this without extra space.
#
#hint: Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0 or (x!=0 and x%10==0)): # x not neg, if x= 10,100,1000,....
            return False
        rev = 0
        while (x>rev):
            rev = rev *10 + x%10   # creating the reverse number using the digits
            x = x/10
        return x==rev or x==rev/10   # if x == rev,  when x = 1 to 9 have to divide with 10
