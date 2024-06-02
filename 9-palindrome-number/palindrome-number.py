class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst=[x for x in str(x)]
        for i in range(0,len(lst)):
            if(lst[i]!=lst[len(lst)-i-1]):
                return False
        return True
        