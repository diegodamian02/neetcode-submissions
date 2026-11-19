class Solution:
    def isPalindrome(self, s: str) -> bool:

        s1 = ""

        for c in s:
            if c.isalnum():
                s1+= c
        
        s1 = s1.lower()
        
        left, right = 0, len(s1) - 1

        while left < right:
            print(s1[left], s1[right])
            if s1[left] == s1[right]:
                left += 1
                right -= 1

            else:
                return False
        
        return True

        

        