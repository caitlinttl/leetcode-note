class Solution(object):
   def convertToBase7(self, n):
        if n < 0: return '-' + self.convertToBase7(-n)
        if n < 7: return str(n)
        return self.convertToBase7(n // 7) + str(n % 7)

n = 100
ans = Solution().convertToBase7(n=n)
print(ans)