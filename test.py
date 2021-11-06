import collections
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        print('-----------------------------')
        print(f's now is: {s}')
        count = collections.Counter(s)
        print(count)
        st = 0
        maxst  = 0
        for i, n in enumerate(s):
            print('---In enumerate---')
            print(f's now is: {s}')
            print(f'enumerate: i={i}, n={n}')
            print(f'count of "{n}" is {count[n]}')
            if count[n] < k: # break string!
                print('count < k, break str.!!!!')
                print(f'maxst: {maxst}')
                print(f'st is: {st}, i is: {i}')
                maxst = max(maxst, self.longestSubstring(s[st:i], k))
                print('leave recursion')
                print(f'maxst: {maxst}')
                print(f'st is: {st}, i is: {i}')
                st = i + 1
            print(f'st: {st}')
        
        # return len(s) if st == 0 else max(maxst, self.longestSubstring(s[st:], k))
        print('---return---')
        print(f'st: {st}')
        if st == 0:
            return len(s)
        else:
            print(f'maxst: {maxst}')
            print(f'st is: {st}')
            return max(maxst, self.longestSubstring(s[st:], k))

        

s = "acbfbfffcbcdbdfffffffffffffffft"
k = 3
ans = Solution().longestSubstring(s=s, k=k)
print(ans)


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = collections.Counter(s)
        st = 0
        maxst = 0
        for i, n in enumerate(s):
            if count[n] < k:
                maxst =  max(maxst, self.longestSubstring(s[st:i], k))
                st = i + 1
        return len(s) if st == 0 else max(maxst, self.longestSubstring(s[st:], k))


s = "acbfbfffcbcdbdfffffffffffffffft"
k = 3
ans = Solution().longestSubstring(s=s, k=k)
print(ans)