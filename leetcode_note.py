class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str=str(x)
        x_rev=str(x)[::-1]
        if x < 0:
            return False
        if x_str == x_rev:
            return True
        else:
            return False
        
        
# ans=Solution().isPalindrome(x=-78187)    
# print(ans)
        

class Solution:
    def searchInsert(self, nums, target) -> int:
        print(nums)
        nums.append(target)
        print(nums)
        nums.sort()
        print(nums)
        a=nums.index(target)
        print(a)
        return a


nums = [1,3,5,6]
target = 4
# ans=Solution().searchInsert(nums=nums,target=target)
# print(ans)


class Solution:
    def removeElement(self, nums, val) -> int:
        while val in nums:
            nums.remove(val)
        print(nums)
        return len(nums)
        # a=[]
        # for i in nums:
        #     print(i)
        #     if i == val:
        #         pass
        #     else:
        #         a.append(i)
        # nums=a
        # print(nums)
        # return (len(a))

nums=[6,6,6,6,7]
val=6
# ans=Solution().removeElement(nums=nums,val=val)
# print(ans)


class Solution:
    def longestCommonPrefix(self, strs):
        ans=""
        for i in zip(*strs):
            if len(set(i))==1:
                ans+=i[0]
            else:
                break
        return ans


class Solution:
    def threeSumClosest(self, nums, target):
        a=[]
        for i in nums:
            print("i= "+str(i))
            nums.remove(i)
            print(nums)
            print('------')


# nums = [-1,2,1,-4]
# target = 1
# ans=Solution().threeSumClosest(nums=nums,target=target)
# print(ans)


# class Solution:
#     def removeDuplicates(self, nums):
#         nums=list(set(nums))
#         print(nums)
#         print(type(nums))
#         return len(nums)

#         nums[:]=sorted(list(set(nums)))
#         return len(nums)


# nums = [0,0,1,1,1,2,2,3,3,4]
# ans=Solution().removeDuplicates(nums=nums)
# print(ans)
        
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[:]
# print(a)


# class Solution:
#     def plusOne(self, digits):
#         a=''
#         for i in digits:
#             a=a+str(i)
#         ans=str(int(a)+1)
#         print(type(ans))
#         print(ans)

#         ans_map=map(int, ans)
#         anss=list(ans_map)
#         print(anss)
#         return(ans)

# digits = [4,3,2,1]
# ans=Solution().plusOne(digits=digits)
# print(ans)

""" class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[]
        for i in range(1,numRows+1):
            if i == 1:
                b=[1]
            elif i == 2:
                b=[1,1]
            elif i == 3:
                b=[1,2,1]
            else:
                tmp=[]
                for j in range(i-2):
                    x=b[j]
                    print("x: " +str(x))
                    u=j+1
                    y=b[u]
                    print("y: " +str(y))
                    z=int(x+y)
                    tmp.append(z)
                b=[1]
                for k in range(i-2):
                    b.append(tmp[k])
                b.append(1)
            a.append(b)
        return a """


class Solution:
    def climbStairs(self, n):
        if n>=1 and n<=45:
            way=[1,2]
            for i in range(43):
                # index_x, index_y=i, i+1 
                # x, y=way[index_x], way[index_y]
                x, y=way[i], way[i+1]
                z=int(x+y)
                way.append(z)
            print(way)
            return way[n-1]
               
            #     1,2,3,5,8,13,21,34

            # if n == 1:  #ans=1
            #     way=[[1]]
            # elif n == 2: #ans=2
            #     way=[[1,1],[2]]
            # elif n == 3:  #ans=3 (2+1)
            #     way=[[1,1,1],[2,1],[1,2]]
            # else:
            #     a=[]
            #     a.append()
            #     n=4  ans=3+2=5
            #     n=5  ans=5+3=8
            #     n=6  ans=8+5=13
            #     n=7  ans=13+8=21

            
n=3
ans=Solution().climbStairs(n=n)
print(ans)


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        if len(nums) >= 1 and len(nums) <= (10**5):
            for i in range(len(nums)):
                if not nums[i] in ans:
                    for j in range(i+1,len(nums)):
                        if nums[i] == nums[j]:
                            ans.append(nums[i])
        return ans


        ans = []
        if len(nums) >= 1 and len(nums) <= (10**5):
            for i in range(len(nums)):
                tmp = nums[i]
                nums[i] = 0
                if tmp in nums:
                    ans.append(tmp)
            return ans

        ans = []
        for key, count in Counter(nums).items():
            if count == 2:
                ans.append(key)
        return ans

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = set()
        duplicates = []
        for i in range(len(nums)):
            currentNum = nums[i]
            if currentNum in visited:
                duplicates.append(currentNum)
            visited.add(currentNum)
        return duplicates
    
    
# Set
# Map => dict

a = [4,3,2,7,8,2,3,1,...............,10]
for i in a:
    if(i == 8):
        print('yay!')
        return
    
    # worst case runtime: 8
    # best case: 1
    # runtime: O(n)

a = [6, 5, 4, 3, 2]
     5, 6, 4, 3, 2
     5, 4, 6, 3, 2
        ...
     5, 4, 3, 2, 6
b = []
for i in len(a):
    for
O(n^2)
O(2*n)

# Runtime complexity O(1)
# Space complexity

def hi():
    return 'hi!!'




class Solution:
    def isHappy(self, n):
        str_n = str(n)
        current = 0
        count = 0
        exist_str = []
        while str_n != '1':
            for i in str_n:
                print("i: "+i)
                current = current + int(i)**2
            print(current)
            str_n = str(current)
            print('str_n is '+str_n)
            current = 0
            if str_n in exist_str:
            # if count == 99: # TODO magic number ?!
                print('exist: '+str_n)
                break
            exist_str.append(str_n)
        if str_n == '1':
            return True
        else:
            return False


class Solution:
    def countPrimes(self, n):
        if n >= 0 and n <= 5*(10**6):
            primes = set()
            if n <= 2:
                return 0
            n = n-1
            for i in range(2,n+1):
                if i == 2 or i % 2 != 0:
                    # print('i: '+str(i))
                    primes.add(i)
                    for p in primes:
                        # print('p: '+str(p))
                        if  i % p == 0 and i / p != 1:
                            # print(f'{i} is not primes')
                            primes.remove(i)
                            break
                        # else:
                        #     if i not in primes:
                        #         # print(f'append {i}')
                        #         primes.append(i)

                    # for j in range(1, i):
                    #     print('j: '+str(j))
                    #     quotient = i / j 
                    #     remainder = i % j
                    #     if j != 1 and quotient != 1 and remainder == 0:
                    #         print(str(i)+' is not primes')
                    #         primes.remove(i)
                    #         break 
                    #     if quotient == i and remainder == 0:
                    #         print(str(i)+' is primes')
                    #         primes.append(i)
            print(primes)
            return len(primes)

        
# Note: "Output Limit Exceeded" >> Not print.
            
n = 99
ans = Solution().countPrimes(n=n)
print(ans)
                    

class Solution:
    def countPrimes(self, n):
        if n <=2:
            return 0
        
        primes = [True] * n
        primes[0] = primes [1] = False

        for number in range(2,n):
            if primes[number]:
                for multiple in range(2*number, n, number):
                    primes[multiple] = False
        return sum(primes)

class Solution:
    def isIsomorphic(self, s, t):
        d = set(zip(s, t))
        print(d)
        print(set(s))
        print(set(t))
        print(len(d))
        print(len(set(s)))
        print(len(set(t)))
        if len(d) == len(set(s)) == len(set(t)):
            return True
        else: return False


# singly-linked list 
# doubly-linked list Runtime complexity O(1)
ListNode:
  self.val = val
  self.next = next
  self.prev = prev
  
  
  0x1: {val: 100, next: 0x100, prev: ???}
  0x2: {......}
  ....
  0x100: {val: 101, next: ??, prev: 0x1}

# List會占用全部的記憶體去貯存資料
# nodeList不需要, 他會用箭頭(next, prev)去做指向, 會多占用一個記憶體去存next(and prev)的資料

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode()
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
                
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
            
        return dummy.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        dum = ListNode(None)
        prev = dum
        
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        if l1 == None:
            prev.next = l2
        elif l2 == None:
            prev.next = l1
        
        return dum.next


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a = []
        for i in range(1,rowIndex+2):
            if i == 1:
                b = [1]
            elif i == 2:
                b = [1,1]
            elif i == 3:
                b = [1,2,1]
            else:
                tmp = []
                for j in range(i-2):
                    this_num = b[j]
                    next_num = b[j+1] 
                    s  = int(this_num + next_num)
                    tmp.append(s)
                # print('tmp: '+str(tmp))
                b = [1]
                for k in range(i-2):
                    b.append(tmp[k])
                b.append(1)
            a.append(b)
        print(a)
        
        return a[rowIndex]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]: # if current price is lower than buy price, change buy price
                buy = i
            else:
                diff = prices[i] - prices[buy] # if current price is higher than buy price, count the profit
                if diff > profit:              # if profit is higher than current_max_profit, change the max_profit.
                    profit = diff
        return profit
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        buy = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                diff = prices[i] - prices[buy]
                profit.append(diff)
                buy = i
        print(profit)
        return sum(profit)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = (''.join(x for x in s if x.isalpha() or x.isdigit())).lower()
        b = a[::-1]
        if a == b:
            return True
        else: return False

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        b = list(a)
        b.sort()
        # print(b)
        count = 0
        ans = []
        for i in range(len(b)):
            # print(i)
            count += 1
            # print('i: '+str(b[i]))
            if i != len(b)-1:
                if b[i] != b[i+1] -1:
                    ans.append(count)
                    # print('count: '+str(count))
                    count = 0
            else:
                    if count != 1:
                        ans.append(count)
                    # print('count: '+str(count))
        # print(ans)
        ans.sort()
        ans.reverse()
        # print(ans)
        return ans[0]


class Solution:
    def longestConsecutive(self, nums):
        if nums == []:
            return 0
        set_nums = set(nums)
        print(set_nums)
        min_num = min(set_nums, default=0)
        set_nums.remove(min_num)
        print(min_num)
        tmp = 1
        ans = []
        for i in set_nums.copy():
            if min_num+1 in set_nums:
                tmp += 1
                set_nums.remove(min_num+1)
                if len(set_nums) == 0:
                    ans.append(tmp)
                    break
                print(set_nums)
                min_num += 1
            if not min_num+1 in set_nums:
                ans.append(tmp)
                min_num = min(set_nums, default=0)
                print(f'now min is: {min_num}')
                if len(set_nums) == 0:
                    break
                set_nums.remove(min_num)
                tmp = 1
                
        print(ans)
        return max(ans, default=1)

        
# nums =  [9,1,4,7,3,-1,0,5,8,-1,6]
# nums =  [-8,-4,9,9,4,6,1,-4,-1,6,8]
nums =  [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
# nums = [100,4,200,1,3,2]
ans = Solution().longestConsecutive(nums=nums)
print(ans)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_nums = set(nums)
        count = 0
        for i in set_nums:
            tmp = nums.count(i)
            if tmp > count:
                count = tmp
                ans = i
        return ans
            

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(1,k+1):
                if i+j < len(nums):
                    if nums[i] == nums[i+j]:
                        print(i,j)
                        print(nums[i],nums[i+j])
                        return True
        return False
                

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            current = nums[0]
            # print(current)
            nums.remove(current)
            # print(nums)
            if current in nums:
                index_i = nums.index(current)
                # print(index_i)
                if index_i < k:
                    return True
        return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_dict = {}
        for i, n in enumerate(nums):
            if n in index_dict:
                if i - index_dict[n] <= k:
                    return True
            index_dict[n] = i
            # print(index_dict)
        return False
                

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 0
        while True:
            tmp = 2 ** x
            if tmp == n:
                return True
            elif tmp > 2 ** n:
                return False
            else:
                x += 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        while n > 1:
            n = n / 2
            if n == 1:
                return True
            if n < 1:
                return False
                
                

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
            
        