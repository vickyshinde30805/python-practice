class Solution:
    def is_alpha(self,s,i):
        x=ord(s[i])
        if 97<=x<=122 or 48<=x<=57:
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        s="A man, a plan, a canal: Panama"
        s=s.lower()
        n=len(s)
        i,j=0,n-1
        while i<j:
            if not self.is_alpha(s,i):
                i+=1
                continue
            if not self.is_alpha(s,j):
                j-=1
                continue
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        