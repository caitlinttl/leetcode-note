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


nums = [-1,2,1,-4]
target = 1
ans=Solution().threeSumClosest(nums=nums,target=target)
print(ans)


class Solution:
    def removeDuplicates(self, nums):
        nums=list(set(nums))
        print(nums)
        print(type(nums))
        return len(nums)

        nums[:]=sorted(list(set(nums)))
        return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
ans=Solution().removeDuplicates(nums=nums)
print(ans)
        
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[:]
print(a)


class Solution:
    def plusOne(self, digits):
        a=''
        for i in digits:
            a=a+str(i)
        ans=str(int(a)+1)
        print(type(ans))
        print(ans)

        ans_map=map(int, ans)
        anss=list(ans_map)
        print(anss)
        return(ans)

digits = [4,3,2,1]
ans=Solution().plusOne(digits=digits)
print(ans)

class Solution:
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
        return a


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


# 204. Count Primes Medium ---------------------------------------

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
                    
# openbook
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


# singly-linked list O(n)
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
            

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                return False
                
        return True


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly_list = [1]
        a = 2
        while len(ugly_list) < n:
            i = a
            while i != 1:
                if i % 2 == 0:
                    i = i / 2
                elif i % 3 == 0:
                    i = i / 3
                elif i % 5 == 0:
                    i = i / 5
                else:
                    a += 1
                    break
            else:
                ugly_list.append(a)
                a += 1
        print(ugly_list)
        return ugly_list[n-1]
        
        

class Solution:
    def nthUglyNumber(self, n):
        multiply_2, multiply_3, multiply_5 = 0, 0, 0
        ugly_number_list = [1]
        list_index = 1
        while list_index < n:
            next_ugly_number = min(ugly_number_list[multiply_2]*2, ugly_number_list[multiply_3]*3, ugly_number_list[multiply_5]*5)
            if next_ugly_number == ugly_number_list[multiply_2]*2:
                print(f'multiply_2: {multiply_2}')
                print(ugly_number_list[multiply_2])
                multiply_2 += 1
            if next_ugly_number == ugly_number_list[multiply_3]*3:
                print(f'multiply_3: {multiply_3}')
                print(ugly_number_list[multiply_3])
                multiply_3 += 1
            if next_ugly_number == ugly_number_list[multiply_5]*5:
                print(f'multiply_5: {multiply_5}')
                print(ugly_number_list[multiply_5])
                multiply_5 += 1
            print(f'next_ugly_number: {next_ugly_number}')
            ugly_number_list.append(next_ugly_number)
            list_index += 1
            print(ugly_number_list)
            print()
        return ugly_number_list[n-1]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while 0 in nums:
            nums.remove(0)
            nums.append('a')
        nums[:] = [ 0 if x == 'a' else x for x in nums]
        # Remove all elements from list
        
        
        
# 290 easy ---------------------------------------
class Solution:
    def wordPattern(self, pattern, s):
        s_list = s.split()
        print(set(pattern))
        print(set(s_list))
        print(set(zip(pattern, s_list)))
        if len(pattern) != len(s_list):
            return False
        if len(set(pattern)) != len(set(s_list)):
            return False
        if len(set(pattern)) != len(set(zip(pattern, s_list))):
            return False
        return True



pattern = "abba"
s = "dog cat cat dog"
ans = Solution().wordPattern(pattern=pattern, s=s)
print(ans)


# 292 easy ---------------------------------------

class Solution:
    def canWinNim(self, n: int) -> bool:
        dict = {1:True, 2:True, 3:True} false true true true false 
        for i in range(4,n+1):
            if dict[i-1] == dict
            dict[i] = 
        return dict[n]
# return false if n % 4 == 0
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n < 4 or n % 4 != 0:
            return True
        else:
            return False

class Solution:
    def canWinNim(self, n: int) -> bool:
        # if n < 4:
        #     return True
        if n % 4 == 0:
            return False
        else:
            return True


# 345 easy ---------------------------------------
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        index_list = []
        vowels_list = []
        index = 0
        for i in list(s):
            if i in vowels:
                index_list.append(index)
                vowels_list.append(i)
            index += 1
        index_list.reverse()
        for j in range(len(index_list)):
            s = list(s)
            s[index_list[j]] = vowels_list[j]
        s = ''.join(s)
        return s
                
        
        
# Sort Algorithm
""" 
The space complexity is a measure of how much "extra" memory your algorithm requires.
If you were to allocate an "extra" array of size n (when n is the variable size of the input array), the space complexity would be O(n).
"""

# 氣泡排序
# Big O: Time Complexity: O(n^2), Space Complexity: O(1)  <---- "extra"
# Worst-case space complexity
# O(n) total, O(1) auxiliary
""" 
比較相鄰的元素。 如果第一個比第二個大，就交換他們兩個。
對每一對相鄰元素作同樣的工作，從開始第一對到結尾的最後一對。 這步做完後，最後的元素會是最大的數。
針對所有的元素重複以上的步驟，除了最後一個。
持續每次對越來越少的元素重複上面的步驟，直到沒有任何一對數字需要比較。
 """
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 選擇排序
# Big O: Time Complexity: O(n^2), Space Complexity: O(1)
""" 
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
再從剩餘未排序元素中繼續尋找最小（大）元素，然後放到已排序序列的末尾。
重複第二步，直到所有元素均排序完畢。
 """
def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 記錄最小數的索引 
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小數時，將 i 和最小數進行交換 
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

# 插入排序
# Big O: Time Complexity: O(n^2), Space Complexity: O(1)
""" 
將第一待排序序列第一個元素看做一個有序序列，把第二個元素到最後一個元素當成是未排序序列。
從頭到尾依次掃描未排序序列，將掃描到的每個元素插入有序序列的適當位置。 （如果待插入的元素與有序序列中的某個元素相等，則將待插入元素插入到相等元素的後面。 ）
 """
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1 
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1 
        arr[preIndex+1] = current
    return arr

# 345 medium ---------------------------------------

nums = [1,1,1,2,2,3]
k = 2

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        print(Counter(nums)) # Counter({1: 3, 2: 2, 3: 1})
        print(Counter(nums).most_common(k)) # [(1, 3), (2, 2)]
        print(dict(Counter(nums).most_common(k))) # {1: 3, 2: 2}
        return dict(Counter(nums).most_common(k)).keys() # dict_keys([1, 2])
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		return dict(Counter(nums).most_common(k)).keys()


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        dict_count = {}
        for i in set_nums:
            count = nums.count(i)
            dict_count[i] = count
        count_list = []
        for c in dict_count.values():
            count_list.append(c)
        count_list.sort()
        count_list.reverse()
        ans = []
        # print(dict_count)
        # print(count_list)
        for i in range(k):
            count = count_list[i]
            for k in dict_count.keys():
                if dict_count[k] == count:
                    if not k in ans:
                        ans.append(k)
        return ans
            

# 357. Count Numbers with Unique Digits Medium ---------------------------------------
# time limit exceeded
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = []
        for i in range(10 ** n):
            ans.append(i)
            for j in list(str(i)):
                if list(str(i)).count(j) != 1:
                    ans.remove(i)
                    break
        print(ans)
        return len(ans)

# openbook
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # f(0) = 1
        # f(1) = 9 + f(0) = 10
        # f(2) = 9 * 9 + f(1) = 91
        # f(3) = 9 * 9 * 8 + f(2) = 739
        
        ans = [1, 10]
        tmp = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(2,n+1):
            num = 1
            for j in range(i):
                num *= tmp[j]  # num = 9, nums = 81
            num += ans[i-1] # num = 81 + 10 = 91
            ans.append(num)
        return ans[n]


# 367 easy ---------------------------------------
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans = num ** 0.5
        return ans.is_integer()
            
        
            
            
# 371. Sum of Two Integers Medium ---------------------------------------
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum((a,b))
        

# 343. Integer Break Medium ---------------------------------------
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)
        for i in range(3, n+1):
            pruduct = 1
            for j in range(1, i):
                print(pruduct)
                # print(dp[j]*(i-j))
                print(f'now i is: {i}')
                print(f'now j is: {j}')
                print(f'now i-j is: {i-j}')
                print(f'now dp[j] is: {dp[j]}')
                print(dp[j]*(i-j)) # 利用前高來算 (加起來要是x的情況, 之前最高是這樣, 再乘以扣掉的, 是否是最高?)
                print((i-j)*j) # 是否創造更高?
                pruduct = max(pruduct, dp[j]*(i-j), (i-j)*j)
                print(f'now product: {pruduct}')
            dp[i] = pruduct
            print(dp)
        return dp[n]
        
# openbook
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)
        for i in range(3, n+1):
            product = 1
            for j in range(1, i):
                product = max(product, dp[j]*(i-j), (i-j)*j)
            dp[i] = product
        return dp[n]

n = 12
ans = Solution().integerBreak(n=n)
print(ans)

# 387.  First Unique Character in a String Easy ---------------------------------------

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in list(s):
            count = list(s).count(i)
            if count == 1:
                return s.index(i)
        return -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = []
        set_s = set(list(s))
        for i in set_s:
            count = list(s).count(i)
            if count == 1:
                index = s.index(i)
                ans.append(index)
                
        if ans == []:
            return -1
        else:
            return min(ans)
            

# 389.   Find the Difference Easy ---------------------------------------
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in list(s):
            t = t.replace(i,"",1) # default arg "count" is max.
        return t
        
        
# 390.   Elimination Game Medium ---------------------------------------
# 
class Solution(object): # Memory Limit Exceeded !!
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        arr = []
        for i in range(1, n+1):
            arr.append(i)
        while len(arr) > 1:
            del arr[::2]
            if len(arr) == 1:
                return arr[0]
            del arr[::-2]
            if len(arr) == 1:
                return arr[0]

""" 
<2的幾次方 決定移動幾次
移動奇數次 頭+2的(次數-1)次方
移動偶數次 當前數量是偶數 頭不變化
          當前數量是奇數  頭+2的(次數-1)次方


50
5次
第一次 2 25
第二次 4 12
第三次 8 6
第四次 8
第五次8+16=24

 """

 
 class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        ans = 1
        while n >= 2**count:
            count += 1
        count -= 1
        print(count)
        for i in range(1, count+1):
            if i % 2 != 0:
                ans += 2**(i-1)
            elif i % 2 == 0:
                if n % 2 == 0:
                    pass
                elif n % 2 != 0:
                    ans += 2**(i-1)
            n = int(n/2)
        return ans


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        i = 1
        while n != 1:
            if i % 2 != 0: # i is odd
                ans += 2**(i-1)
            else: # i is even
                if n % 2 != 0: # n is odd
                    ans += 2**(i-1)
            n = int(n/2)
            i += 1
        return ans
        return True


# 392. Is Subsequence Easy ---------------------------------------
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0
        list_t = list(t)
        a = 0
        for i in list(s):
            print(i)
            if a != 0:
                del list_t[0:index+1]
            print(list_t)
            if not i in list_t:
                return False
            else:
                index = list_t.index(i)
            print(index)
            a = 1


        

# 397. Integer Replacement Medium ---------------------------------------
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 1:
            if n % 2 != 0:
                if ((n-1)/2) % 2 == 0 or (n-1) == 2:  # is even
                    n -= 1
                else:
                    n += 1
            else:
                n /= 2
            count += 1
        return count
                    
# 400. Nth Digit Medium ---------------------------------------
class Solution(object): # Time Limit Exceeded
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = []
        for i in range(1,n+1):
            tmp.append(str(i))
            if len(''.join(tmp)) > n:
                break
        return str(''.join(tmp))[n-1]

class Solution(object): # Time Limit Exceeded
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = ""
        for i in range(1,n+1):
            a += str(i)
            if len(a) > n:
                break
        return a[n-1]


# 409. Longest Palindrome Easy ---------------------------------------
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = False
        nums = list(s)
        set_list = set(nums)
        print(set_list)
        
        ans = 0
        for i in set_list:
            print(i)
            count_i = nums.count(i)
            print(count_i)
            count = (count_i)/2
            print(count)
            if count >= 1:
                ans += count*2
            if count_i % 2 == 1:
                single = True
        if single == True:
            ans += 1

        return int(ans)

s = "a"
ans = Solution().longestPalindrome(s=s)
print(ans)



# 395. Longest Substring with At Least K Repeating Characters Medium ---------------------------------------
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


# openbook
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

        
# 350. Intersection of Two Arrays II Easy ---------------------------------------


import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count_1 = collections.Counter(nums1)
        count_2 = collections.Counter(nums2)
        ans = []

        for n in set(nums1):
            if n in set(nums2):
                min_repeat = min(count_1[n], count_2[n])   
                for i in range(min_repeat):
                    ans.append(n)
        return ans
                
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
ans = Solution().intersect(nums1=nums1, nums2=nums2)
print(ans)



# 374. Guess Number Higher or Lower Easy ---------------------------------------

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(n):
    pick = 50
    if pick == n:
        return 0
    elif pick > n:
        return 1
    elif pick < n:
        return -1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        response = 2
        if guess(1) == 0:
            return 1            
        elif guess(n) == 0:
            return n            
        while response != 0:
            print(f'low is {low}')
            print(f'high is {high}')
            tmp = int((high+low)/2)
            response = guess((tmp))
            response2 = guess((tmp+1))
            if response == 0:
                return tmp
            elif response2 == 0:
                return tmp+1
            elif response == 1:
                low = tmp
            elif response == -1:
                high = tmp

n = 1000
pick = 56
ans = Solution().guessNumber(n=n)
print(ans)



# 413. Arithmetic Slices Medium---------------------------------------

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        count = 0
        for i in range(len(nums)-2): # i = 1, 3, 5
            print('i now is:' + str(i))
            dif_list = []
            for j in range(i+1, len(nums)): # when i = 1, j = 3, 5, 7, 9, when i = 3, j = 5, 7, 9
                print(nums[j])
                print(nums[j-1])
                dif = nums[j] - nums[j-1] # dif = 3-1, 5-3, 7-5, dif = 5-3, 7-5, 9-7
                print(dif)
                dif_list.append(dif)
                print(dif_list)
                if len(dif_list) >= 2 and len(set(dif_list)) == 1:
                    count += 1
                if len(set(dif_list)) != 1:
                    break
            print('count now is:' + str(count))
        return count

# less time complexity.
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        curr = 0
        sum = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]: 
                curr += 1 
                # 321 432(4321) 543(5432)(54321) 654(6543)(65432)(654321) 
                # 多的組合是最大的數字組成的三位, 其他組合則是上一個加上最大的數字
                sum += curr
            else:
                curr = 0
        return sum

                
            
nums = [1,2,3,4,5]
nums = [7,7,7,7]
nums = [1,3,5,7,9]


# 414. Third Maximum Number Easy---------------------------------------
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = sorted(list(set(nums)))
        print(tmp)
        if len(tmp) < 3:
            return max(tmp)
        else:
            return tmp[-3]

# use sorted's argument "reverse = Ture"
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lst = sorted(list(set(nums)),reverse = True)
        return lst[2] if len(lst) > 2 else lst[0]


# 415. Add Strings Easy---------------------------------------

openbook
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum = 0
        count = 0
        for i in num1[-1::-1]:
            sum += int(i) * (10 ** count)
            count += 1
        
        count = 0
        for j in num2[-1::-1]:
            sum += int(j) * (10 ** count)
            count += 1
            
        return str(sum)



# 434. Number of Segments in a String Easy ---------------------------------------

class Solution:
    def countSegments(self, s: str) -> int:
        list_s = s.split(' ')
        list_s[:] = (x for x in list_s if x != '')
        # Remember !! The syntax of remove all elements from list
        # 從list移除某值的方法
        # [i for i in x if i != 2]
        # while 2 in x: x.remove(2)
        # nums[:] = [ 0 if x == 'a' else x for x in nums]
        return len(list_s)
        

s = "Hello, my name is John"
s = "Hello"
s = "love live! mu'sic forever"
s = ""                # should return 0 
s = "           "     # should return 0 

# 441. Arranging Coins Easy---------------------------------------


class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = 0
        i = 0
        while n >= coins: # Be care for the "=" is needed.
            i += 1
            coins += i
        return i-1


# 448. Find All Numbers Disappeared in an Array Easy---------------------------------------
# Remember !!
# list不能直接相減, 但是set可以相減!!!!
# unsupported operand type(s) for -: 'list' and 'list'
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all = []
        for i in range(1, len(nums)+1):
            all.append(i) 
        ans = (set(all)-set(nums))        
        return ans

# 451. Sort Characters By Frequency Medium---------------------------------------

import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        count = collections.Counter(list(s)).most_common()
        for i, n in count:
            # print(i ,n)
            ans += i*n
        # return (''.join(ans))
        return ans

        

s = "treeAAABvvWWWWW"
ans = Solution().frequencySort(s=s)
print(ans)


# str to list
s = 'apple'
print(list(s))

# list join to str
s = ['a', 'p', 'p', 'l', 'e']
print(''.join(s))


# 423. Reconstruct Original Digits from English Medium---------------------------------------
import collections
# openbook
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        count = collections.Counter(s)
        # print(count)
        if "z" in count:
            ans += "0" * count["z"]
        if "o" in count:
            tmp = count["o"] - count["z"] - count["w"] - count["u"]
            ans += "1" * tmp
        if "w" in count:
            ans += "2" * count["w"]
        if "h" in count:
            tmp = count["h"] - count["g"]
            ans += "3" * tmp
        if "u" in count:
            ans += "4" * count["u"]
        if "f" in count:
            tmp = count["f"] - count["u"]
            ans += "5" * tmp
        if "x" in count:
            ans += "6" * count["x"]
        if "s" in count:
            tmp = count["s"] - count["x"]
            ans += "7" * tmp
        if "g" in count:
            ans += "8" * count["g"]
        if "i" in count:
            tmp = count["i"] - (count["f"] - count["u"]) - count["x"] - count["g"]
            ans += "9" * tmp

        return ans

"""         
["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]

zero
one
two
three
four
five
six
seven
eight
nine

0:z
2:w
4:u
6:x
8:g
5 = f - 4
7 = s - 6
3 = h - 8
1 = o - 0 - 2 - 4
9 = i - 5 - 6 - 8

5,7:v
6,7:s
3,4:r
3,8:h
4,5:f
2,3,8:t
1,7,9:n
0,1,2:o
5,6,8,9:i
0,1,3,5,7,8,9:e 

"""


s = "fviefuro"
ans = Solution().originalDigits(s=s)
print(ans)






# 452. Minimum Number of Arrows to Burst Balloons Medium---------------------------------------
# openbook
# package: lambda
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key = lambda x : x[1])  # The index must be "1", 
        # 因為是"射在最大值上面"，所以要去排列的，是氣球的大值(往右的胖度)，小值不照順序沒關係只是這顆氣球(往左)比較胖，但是大值要照順序。
        print(points) # [[1, 6], [2, 8], [7, 12], [10, 16]]
        arrow = 0
        arrow_last_hit = -float('inf') # 負無窮大
        for each in points:
            if each[0] > arrow_last_hit : # 1 > -inf, 2 < 6, 7 > 6, 10 < 12
                arrow += 1
                arrow_last_hit = each[1] #hit = 6            hit = 12
                print(arrow_last_hit)
        print(arrow)


points = [[10,15],[2,8],[9,16],[16,17]]
ans = Solution().findMinArrowShots(points=points)
print(ans)

# 453. Minimum Moves to Equal Array Elements Medium---------------------------------------

# 用數學的方法，需要加總的數字(move)，會等於排序好的數列的"每一個值"依序去減最小值 的總和。
""" 例如
nums = [6, 10, 12, 16]  第一次全部加 16-6=10
nums = [16, 20, 22, 16] 現在最大和最小一樣了，處理第二大的的22，第二次全部加 22-16=6
nums = [22, 26, 22, 22] 第三次全部加 26-22=4
nums = [26, 26, 26, 26] 
答案等於 10+6+4
16-6=10
12-6=6
10-6=4
 """
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        move = 0
        nums = sorted(nums)
        for i in range(len(nums)-1):
            move += nums[-1-i] - nums[0]
        return move

# A smart way !!
class Solution(object):
    def minMoves(self, nums):
        return sum(nums) - len(nums)*min(nums)

        
        
# time limit exceeded
# 每次都去處理數列加diff, 太慢了
class Solution(object):
    def minMoves(self, nums):
        move = 0
        while len(set(nums)) != 1:
            diff =  max(nums) - min(nums)
            # print(diff)
            # 數列的值全部相加某數的方法
            nums = [i+diff for i in nums] # way1
            # nums = map(lambda x:x+diff, nums) # way2
            # for i in range(len(nums)): # way3
            #     nums[i] += diff
            index = nums.index(max(nums))
            nums[index] -= diff
            move += diff
            
        return move
        

nums = [383,886,777,915,793,335,386,492]
ans = Solution().minMoves(nums=nums)
print(ans)




# 416. Partition Equal Subset Sum Medium---------------------------------------
# openbook
class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 == 1: return False
            
        target = total / 2   #target sum 
        sums_of_subsets = set([0])         #stores the sums of the subsets 存放已知相加不到target的數字
        print(sums_of_subsets)
        
        for n in nums:
            sums_with_n = []  #stores the sums of the subsets that contain n 存放"已知不到terget且這次加上n也不到target"的數字
            for i in sums_of_subsets:
                if i + n == target: 
                    return True
                if i + n < target:
                    sums_with_n.append(i + n)
            sums_of_subsets.update(sums_with_n) # combine two subsets
                
        return False


# nums = [1,1,2,2,2,4]
nums = [2,5,11,6]
ans = Solution().canPartition(nums=nums)
print(ans)

# 455. Assign Cookies Easy ---------------------------------------
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        cont = 0
        for i in g:
            for j in s:
                if j >= i:
                    s.remove(j)
                    cont += 1
                    break
        return cont

        

# less time complextity
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1 
        return child


# 459. Repeated Substring Pattern Easy---------------------------------------


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sub_str = ""
        for i in s:
            sub_str += i
            if len(sub_str) <= int(len(s))/2 and len(s) % len(sub_str) == 0:
                tmp = sub_str*int(len(s)/len(sub_str))
                if tmp == s:
                    return True
        return False
 
        


# s = "abcabcabcabc"
s = "aabcaabcaabct"
ans = Solution().repeatedSubstringPattern(s=s)
print(ans)



# 463. Island Perimeter Easy---------------------------------------
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        # 算水平重複(垂直的邊界重複)
        for x in grid:
            for index_x in range(len(x)-1):
                if x[index_x] == 1 and x[index_x+1] == 1:
                    count += 1
        # print(count)

        # 算垂直重複(水平的邊界重複)
        for index_x in range(len(grid[0])):
            for index_y in range(len(grid)-1):
                if grid[index_y][index_x] == 1 and grid[index_y+1][index_x] == 1:
                    count += 1
        # print(count) 
        # print(str(grid).count("1"))
        return str(grid).count("1")*4 - count*2
            
            
# grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
grid = [[1,0]]
ans = Solution().islandPerimeter(grid=grid)
print(ans)




# 470. Implement Rand10() Using Rand7() Medium---------------------------------------

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# 7 ** 3 = 343 (>100)

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        tmp = []
        for i in range(1,8):
            for j in range(1, 8):
                for k in range(1, 8):
                    tmp.append([i, j, k])
        rand = [rand7(), rand7(), rand7()]
        index = tmp.index(rand)
        return int((index // 34.3) + 1)  

# openbook
# Rejection Sampling and 升維/降維
# Remember!!
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        rand40 = 40
        while rand40 >= 40:
            rand40 = (rand7() - 1) * 7 + rand7() - 1
        return rand40 % 10 + 1 

# https://www.cnblogs.com/grandyang/p/9727206.html




# 473. Matchsticks to Square Medium---------------------------------------
# openbook
# DFS !!! 
# TODO

class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        sum_len = sum(matchsticks)
        if sum_len % 4 != 0:
            return False
        
        target = sum_len / 4
        print(f'target is: {target}')
        matchsticks.sort(reverse=True)
        # WRONG !!
        # while matchsticks != []:
        #     i = matchsticks[0]
        #     print(matchsticks)
        #     print(f'now i is: {i}')
        #     if i > target:
        #         return False
        #     elif i < target:
        #         find_short = target - i
        #         if find_short not in matchsticks:
        #             return False
        #         else:
        #             print(f'remove short: {find_short}')
        #             matchsticks.remove(find_short)
        #     print(f'remove i: {i}')
        #     matchsticks.remove(i)
        
        # return True
            


# matchsticks = [1,1,2,2,2]   
matchsticks = [5,3,3,1,3,2,3]   
matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]   
ans = Solution().makesquare(matchsticks=matchsticks)
print(ans)




# 475. Heaters Medium---------------------------------------

# openbook
# Remember
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        heaters=[float('-inf')]+heaters+[float('inf')] # add 2 fake heaters
        ans,i = 0,0
        for house in houses:
            while house > heaters[i+1]:  # search to put house between heaters
                i +=1
                print(i)
            print(f'i now is: {i}')
            print(f'heaters[i]: {heaters[i]}')
            print(f'heaters[i+1]: {heaters[i+1]}')
            dis = min (house - heaters[i], heaters[i+1]- house)
            ans = max(ans, dis)
        return ans


# houses = [1,5]
# houses = [1,2,3,4]
# heaters = [1,4]
houses = [1,1,1,200,300,400,997,999]
heaters = [499,500,501]
ans = Solution().findRadius(houses=houses, heaters=heaters)
print(ans)


# 482. License Key Formatting Easy---------------------------------------
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.upper()
        s = s.replace("-","")
        r = len(s) % k
        ans = ""
        ans += s[:r]
        for i in range(r,len(s),k):
            ans += "-" + s[i:i+k]
            
        if r == 0:
            ans = ans[1::]
        return ans
        




# 485. Max Consecutive Ones Easy---------------------------------------

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        count = 0
        ans = []
        for i in nums:
            if i == 1:
                count += 1
            else:
                ans.append(count)
                count = 0
        return max(ans)
        
nums = [1,1,0,1,1,1]

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans, count =0, 0
        for i in nums:
            if i == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        return ans
        

# 492. Construct the Rectangle Easy---------------------------------------

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # print(int(area ** 0.5))
        if area == 1:
            return [1,1]
        ans = [0,0]
        # diff = area
        for l in range((int(area ** 0.5)), area+1):
            w = area / l if area % l == 0 else 0
            if w == 0 or w > l: 
                continue
            else:
                return [l,w]
                
            # tmp_diff = l - w
            # if tmp_diff <= diff:
            #     diff = tmp_diff
                # ans = [l,w]
            # return ans
            
            # for w in range(1, area+1):
            # if l >= w and l*w == area:
            # if l >= w:
            #     tmp_diff = l - w
            #     if tmp_diff < diff:
            #         diff = tmp_diff
            #         return [l,w]

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        ans = [0,0]
        for l in range((int(area ** 0.5)), area+1):
            w = area / l if area % l == 0 else 0
            if w == 0 or w > l: 
                continue
            else:
                return [l,w]
                
# speed up
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area)) # 返回平方根
        # w = int(area ** (0.5))
        # print(w)
        while area % w != 0:
            w -= 1
        return area//w, w
        # return area/w, w
                




# 495. Teemo Attacking Easy---------------------------------------

# time limit exceeded
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans = []
        for i in timeSeries:
            for j in range(duration):
                ans.append(i+j)
        return len(set(ans))

# Use Math solution
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        repeat = 0
        for i in range(len(timeSeries)-1):
            diff = timeSeries[i+1] - timeSeries[i]
            if diff < duration:
                repeat += duration - diff
        return len(timeSeries)*duration - repeat
        



# 496. Next Greater Element I Easy---------------------------------------

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = [-1]*len(nums1)
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            for j in nums2[index::]:
                if j > nums1[i]:
                    ans[i] = j
                    break
        return ans
                
            

# 500. Keyboard Row Easy---------------------------------------

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = [] # Remember not use "ans = words, otherwise the "words" will be changed together."
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        for word in words:
            ans.append(word) 
            pre_group = 0
            for i in lower(word): # python2
                if i in first_row: 
                    group = 1
                elif i in second_row:
                    group = 2
                else:
                    group = 3
                if pre_group != group and pre_group != 0:
                    ans.remove(word)
                    break
                pre_group = group
        return ans
                    

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Remember not use "ans = words, otherwise the "words" will be changed together."
        first_row = "qwertyuiop"
        ans = words.copy() # The ways of copy a list. Remember!!
        ans = words[:]  
        ans = list(words) 
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        for word in words:
            pre_group = 0
            for i in word.lower(): # python3
                if i in first_row:
                    group = 1
                elif i in second_row:
                    group = 2
                else:
                    group = 3
                if pre_group != group and pre_group != 0:
                    ans.remove(word)
                    break
                pre_group = group
        return ans
                    
        
                        
        

# 503. Next Greater Element II Medium---------------------------------------

# 	Time Limit Exceeded!! passed, but took too long.
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [-1]*len(nums)
        nums_repeat = nums*2
        for i in range(len(nums)):
            index = nums_repeat.index(nums[i])
            for j in nums_repeat[index::]:
                if j > nums[i]:
                    ans[i] = j
                    break
            nums_repeat.remove(nums[i])
        return ans
        

# openbook
# Remember
# stack and pop
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack = nums[::-1]
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop() # default index=-1
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
        return ans


nums = [1,2,5,2,4,3]
ans = Solution().nextGreaterElements(nums=nums)
print(ans)

# 506. Relative Ranks Easy---------------------------------------

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        ans = [str(len(score))]*len(score) # for person whe got 0 scare.
        rank = ""
        i = 1
        while sum(score) != 0:
            max_score = max(score)
            index_max = score.index(max_score)
            score[index_max] = 0
            if i == 1:
                rank = "Gold Medal"
            elif i == 2:
                rank = "Silver Medal"
            elif i == 3:
                rank = "Bronze Medal"
            else:
                rank = str(i)
            ans[index_max] = rank
            i += 1
        return ans
        

score = [10,3,8,9,4]
ans = Solution().findRelativeRanks(score=score)
print(ans)

class Solution(object):
    def findRelativeRanks(self, score):

        len_score = len(score)
        ans = [str(len_score)]*len_score
        rank = ""
        i = 1
        while sum(score) != 0:
            max_score = max(score)
            index_max = score.index(max_score)
            score[index_max] = 0
            ans[index_max] = i
            i += 1
            
        rep_list = {1:"Gold Medal", 2:"Silver Medal", 3:"Bronze Medal"}
        ans = [rep_list[x] if x in rep_list else str(x) for x in ans]
        
        return ans

# Remember Zip
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        dunums = sorted(score, reverse=True)
        print(dunums)
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(score))]
        dt = dict(zip(dunums, medal))
        return [dt[i] for i in score]
        


score = [10,3,8,9,4]
ans = Solution().findRelativeRanks(score=score)
print(ans)



# 504. Base 7 Easy---------------------------------------

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        neg = False
        if num == 0:
            return 0
        if num < 0:
            num = 0-num
            neg = True

        tmp = []
        while num // 7 >= 7:
            tmp.append(num % 7)
            num //= 7
        tmp.append(num % 7)
        tmp.append(num // 7)

        ans = 0
        count = 0
        for i in tmp:
            ans += 10**count * i
            count += 1
        
        return str(ans) if neg == False else str(0-ans)

""" 
        100 / 7 = 14 ... 2
        14 / 7 = 2 ... 0
        ans = 2*100 + 0*10 + 2*1 = 202

        -7 / 7 = -1 ... 0
        ans = -1*10 + 0*1 = -10
        
 """

num = -7
ans = Solution().convertToBase7(num=num)
print(ans)


# Iteration and Recursion
class Solution(object):
   def convertToBase7(self, n):
        if n < 0: return '-' + self.convertToBase7(-n)
        if n < 7: return str(n)
        return self.convertToBase7(n // 7) + str(n % 7)



# 507. Perfect Number Easy---------------------------------------

# Time Limit Exceeded!!
# TODO
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        divisor = []
        for i in range(1, num):
            if num % i == 0 and i not in divisor:
                divisor.append(i)
        
        return True if sum(divisor) == num else False
        

# 520. Detect Capital Easy---------------------------------------

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ans = [word.upper(), word.lower(), word[0].upper() + word[1::].lower()]
        # upper = word.upper()
        # lower = word.lower()
        # first = word[0].upper() + word[1::].lower()
        return True if word in ans else False


# By StefanPochmann
class Solution(object):
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()
        return word in [word.upper(), word.lower(), word.capitalize()]



# 540. Single Element in a Sorted Array Medium---------------------------------------
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums))*2 - sum(nums)

        for key, count in Counter(nums).items():
            if count == 1:
                return key


# BinarySearch
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: # For case nums == [1]
            return nums[0]
        left = 0
        right = len(nums) - 1
        mid = int(left + (right - left)/2)
        # print(mid, nums[mid])
        while nums[mid] == nums[mid+1] or nums[mid] == nums[mid-1]:
            # print(left, right)
            mid = int(left + (right - left)/2)
            # print(mid, nums[mid])
            if mid == left and mid != 0: # For case 答案是最右邊的數字
                return nums[mid+1]
            if mid % 2 == 0: # even
                if nums[mid] != nums[mid+1]:
                    right = mid 
                else:
                    left = mid
            if mid % 2 != 0: # odd
                if nums[mid] != nums[mid-1]:
                    right = mid
                else:
                    left = mid
        return nums[mid]
        

nums = [1,1,2,3,3,4,4,8,8]
""" Key Point: 奇數應該要和左邊一樣，偶數應該要和右邊一樣 """
# nums = [3,3,7,7,10,11,11]
# nums = [3,7,7,8,8,10,10,22,22,30,30]
ans = Solution().singleNonDuplicate(nums=nums)
print(ans)

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        low=0
        high=n-1
        
        while low<high:
            mid=(low+high)//2
            
            if (mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
                low=mid+1
            else:
                high=mid
        return nums[low]
                
# 704. Binary Search Easy---------------------------------------
# classical binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int(left + (right-left)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        

# 852. Peak Index in a Mountain Array Easy---------------------------------------
# binary search
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = int(left + (right-left)/2)
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid-1]:
                left = mid + 1
            elif arr[mid] < arr[mid-1]: 
                right = mid - 1
        return -1
        


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i
            
        


# 189. Rotate Array Medium---------------------------------------


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = [1]*n # Can't use 0 for tmp list
        for i in range(n):
            if i + k <= n - 1:
                index = i + k
            else:
                index = (i + k) % n # Key point !!!!!
            tmp[index] = nums[i]
        nums[:] = tmp

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = [1]*n # Can't use 0 for tmp list
        for i in range(n):
            index = (i + k) % n # Key point !!!!!!! 取餘數!!
            tmp[index] = nums[i]
        nums[:] = tmp


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

# 1260. Shift 2D Grid Easy---------------------------------------

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        tmp = []
        for l in grid:
            n = len(l)
            for i in l:
                tmp.append(i)
                
        k = k % len(tmp) # Key point !!
        tmp[:] = tmp[-k:] + tmp[:-k]
        
        ans = []
        count = 0
        sub = []
        for i in tmp:
            count += 1
            sub.append(i)
            if count == n:
                ans.append(sub)
                count = 0
                sub = []
        return ans

        

# 912. Sort an Array Medium---------------------------------------

"""
Runtime: O(nlogn) expected, O(n^2) worst case.
With a proper choice of pivot (using the median of medians algorithm), the runtime can be reduced to strict O(nlogn).
Space: O(n) expected, O(n^2) worst case 
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return(nums)
        
        pivot = random.choice(nums)
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]
        
        return self.sortArray(lt) + eq + self.sortArray(gt)

# 941. Valid Mountain Array Easy---------------------------------------
# Remember 記得要檢查長度和是否最大值在頭尾
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: # 長度小於三不行
            return False
        max_num_index = arr.index(max(arr))
        if arr[max_num_index] == arr[0] or arr[max_num_index] == arr[-1]: # 在頭尾不行
            return False
        for i in range(max_num_index-1):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(max_num_index, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        return True
        


# 228. Summary Ranges Easy---------------------------------------
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        ans = []
        st = nums[0]
        end = nums[0]
        for i in range(len(nums)-1):
            # print(i)
            if nums[i]+1 == nums[i+1]:
                end = nums[i+1]
                conti = True
            else:
                conti = False
                
            if conti == False or i == len(nums)-2:
                # print(st,end)
                if st == end:
                    ans.append(str(st))

                else:
                    tmp = str(st)+"->"+str(end)
                    ans.append(tmp)
                st = nums[i+1]
                end = nums[i+1]
                if i == len(nums)-2 and conti == False:
                    ans.append(str(nums[i+1]))
        return ans
        


# 551. Student Attendance Record I Easy---------------------------------------

class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = s.count('A')
        if 'LLL' in s or a_count >= 2:
            return False
        else:
            return True
        
# Reverse Words in a String III Easy---------------------------------------
class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split(" ")
        print(list_s)
        ans = []
        for i in list_s:
            ans.append(i[::-1])
        ans = " ".join(ans)
        return ans

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(x[::-1] for x in s.split())
        return ' '.join(s.split()[::-1])[::-1]


# 848. Shifting Letters Medium---------------------------------------
# Remember
""" 
chr(97) # 'a'
ord('a') # 97
"""

# Time Limit Exceeded
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        letter_list = list(string.ascii_lowercase)
        s_index = []
        
        # shifts_list = []
        # for i in range(len(shifts)):
        #     shifts_list.append(sum(shifts[i::]))
            
        for i in range(len(shifts)):
            letter = s[i]
            add = sum(shifts[i::])
            new_index = (letter_list.index(letter) + add) % 26
            s_index.append(letter_list[new_index])
        
        return "".join(s_index)
        
# PASS
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        letter_list = list(string.ascii_lowercase)
        s_index = []
        shifts_list = [sum(shifts)]
                    
        for i in range(len(shifts)):
            shifts_list.append(shifts_list[i] - shifts[i]) # DP, 為下一次做準備
            letter = s[i]
            add = shifts_list[i]
            new_index = (letter_list.index(letter) + add) % 26
            s_index.append(letter_list[new_index])
        
        return "".join(s_index)
        


# 75. Sort Colors Medium---------------------------------------
""" 
in-place!!
in-place means that the algorithm does " not use extra(auxiliary ) space" for manipulating
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = nums.count(0)
        count_1 = nums.count(1)
        count_2 = nums.count(2)
        nums[:] = [0]*count_0 + [1]*count_1 + [2]*count_2



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            for j in range(0, len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                
        

# 876. Middle of the Linked List Easy---------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur != None:
            length += 1
            cur = cur.next
        cur = head
        i = 0
        while i < length//2:
            cur = cur.next
            i += 1
        return cur

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow if fast.next == None else slow.next
        
            
            
            


# 237. Delete Node in a Linked List Easy---------------------------------------
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next





# 83. Remove Duplicates from Sorted List Easy---------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        while head == None:
            return head
        cur = head
        next_one = head.next
        while next_one != None:
            if cur.val == next_one.val:
                # print('same')
                cur.next = next_one.next # 相等時, 改變cur的next, 但cur不用前進
                next_one = next_one.next # next_one都前進
            else:
                # print('not_same')
                cur = cur.next # 不相等時, cur才前進
                next_one = next_one.next # next_one都前進
                
            # print(cur)
            # print(next_one)
            # print(head)
            # print('------------')
            
        return head
        
""" 
Your input = [1,2,2,3]

not_same
ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 3, next: None}}}
ListNode{val: 2, next: ListNode{val: 3, next: None}}
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 3, next: None}}}}
-------------
same !!!
ListNode{val: 2, next: ListNode{val: 3, next: None}} // key point!!
ListNode{val: 3, next: None}
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: None}}}
-------------
not_same
ListNode{val: 3, next: None}
None
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: None}}}
-------------

"""




# 82. Remove Duplicates from Sorted List II Medium---------------------------------------


# openbook

""" 
*** use three pointers: pre, cur, post ***
post moves forward to check whether its value is the same with cur.val
if not, these three pointers moves forward together
if yes, post itself moves forward until its value is not same with cur.val
    at this time, cur is at the start of the duplicate value, and post is after the end
    then let pre.next=post
————————————————
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        post = head.next

        while post != None:
            while post != None and post.val != cur.val: 
            # No repeat
                pre = pre.next
                cur = cur.next
                post = post.next
            while post != None and post.val == cur.val: 
            # Repeat, post itself moves forward until its value is not same with cur.val
                post = post.next
            if post != cur.next:
                pre.next = post
                cur = post
                if post != None:
                    post = post.next

        return dummy.next





            

        
        
# 141. Linked List Cycle Easy---------------------------------------
# openbook
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
1. Use two pointers, walker and runner.
2. walker moves step by step. runner moves two steps at time.
3. if the Linked List has a cycle walker and runner will meet at some point.
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if head == None:
            return False
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False



def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False



# 206. Reverse Linked List Easy---------------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        rev = head
        
        tmp = []
        tmp.append(head.val)
        while head.next != None:
            head = head.next
            tmp.append(head.val)
        
        tmp = tmp[::-1]
        
        ans = rev
        for i in range(0, len(tmp)):
            rev.val = tmp[i]
            rev = rev.next
        
        return(ans)

# Iterative !!
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            print('===========')
            print(head)
            
            curr = head
            print(curr)
            
            head = head.next
            print(head)
            
            curr.next = prev
            print(curr)
            
            prev = curr
            print(prev)
        return prev

""" 
===========
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
ListNode{val: 1, next: None}
ListNode{val: 1, next: None}
===========
ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
ListNode{val: 2, next: ListNode{val: 1, next: None}}
ListNode{val: 2, next: ListNode{val: 1, next: None}}
===========
ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
ListNode{val: 4, next: ListNode{val: 5, next: None}}
ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
===========
ListNode{val: 4, next: ListNode{val: 5, next: None}}
ListNode{val: 4, next: ListNode{val: 5, next: None}}
ListNode{val: 5, next: None}
ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
===========
ListNode{val: 5, next: None}
ListNode{val: 5, next: None}
None
ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}
ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}



 """
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head != None:
            cur = head   
            head = head.next
            cur.next = prev
            prev = cur
        return prev



# 278. First Bad Version Easy---------------------------------------


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        if isBadVersion(1) == True:
            return 1

        while True:
            if isBadVersion(n) == True and isBadVersion(n-1) == False:
                return n
        
            n = low + (high-low)//2
            if isBadVersion(n) == True:
                high = n
            elif isBadVersion(n) == False:
                low = n
        


# 34. Find First and Last Position of Element in Sorted Array Medium---------------------------------------

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not target in nums: # No target in nums
            return [-1, -1]
        
        n = len(nums)

        if n == 1: # len = 1 and it's target
            return [0, 0]

        if nums[0] == target and nums[1] != target: # Only the first num is target
            return [0, 0]

        if nums[-1] == target: # The last nums is target
            return [nums.index(target), n-1]

        low = 0
        high = n
        while True:
            n = low + (high-low)//2
            if nums[n] == target and nums[n+1] != target: # Find the last target index
                return [nums.index(target), n]
            if nums[n] > target:
                high = n
            elif nums[n] <= target:
                low = n


# 13. Roman to Integer Easy---------------------------------------

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}
        spec = ["I", "X", "C"]
        for i in range(len(s)):
            
            if i != len(s)-1 and s[i] in spec:
                # print(s[i])
                if s[i] == "C":
                    if s[i+1] == "D" or s[i+1] == "M":
                        ans -= 100
                    else:
                        ans += 100
                if s[i] == "X":
                    if s[i+1] == "L" or s[i+1] == "C":
                        ans -= 10
                    else:
                        ans += 10
                if s[i] == "I":
                    if s[i+1] == "V" or s[i+1] == "X":
                        ans -= 1
                    else:
                        ans += 1
                continue
            
            ans += roman_dict[s[i]]
            
        return ans

# Smart solution
# *Note: The trick is that the last letter is always added. Except the last one, 
# if one letter is less than its next one, this letter is subtracted減去.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}

        for i in range(len(s)-1): # the last letter of s must be add
            if roman_dict[s[i]] < roman_dict[s[i+1]]: # If one letter is less than its next one, this letter is subtracted
                ans -= roman_dict[s[i]]
            else:
                ans += roman_dict[s[i]]
        
        ans += roman_dict[s[-1]] # the last letter of s must be add
        
        return ans
                
            
        


# 476. Number Complement Easy---------------------------------------

class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        comp = ["1" if i == "0" else "0" for i in binary] # put loop behind
        comp = "".join(comp)
        ans = int(comp, 2)
        return ans
        
# 91. Number of 1 Bits Easy---------------------------------------

class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(n)
        return str(bin(n)[2:]).count("1")


# 20. Valid Parentheses Easy---------------------------------------
# openbook
# stack pop

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_p = {"]":"[", ")":"(", "}":"{"}
        for char in s:
            if char in dict_p.values(): # char = [, (, {
                stack.append(char)
            elif char in dict_p.keys(): # char = ], ), }
                if stack == [] or dict_p[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        



# 682. Baseball Game Easy---------------------------------------

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        spec = ["C", "D", "+"]
        for i in ops:
            if not i in spec:
                ans.append(int(i))
            else:
                if i == "C":
                    ans.pop()
                elif i == "D":
                    ans.append(2*ans[-1])
                elif i == "+":
                    ans.append(ans[-1] + ans[-2])
        return sum(ans)
                
        


# 739. Daily Temperatures Medium---------------------------------------

# Time Limit Exceeded
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        while temperatures != []:
            today = temperatures[0]
            if not max(temperatures) > today:
                    ans.append(0)
            else:
                for i in range(len(temperatures)):
                    if temperatures[i] > today:
                        ans.append(i)
                        break
            temperatures.pop(0)
        return ans
            
        
                
# stack
# openbook

""" 
Improved from the stack solution, which iterates backwards.
We itereate forward here so that enumerate() can be used.
Everytime a higher temperature is found, we update answer of the peak one in the stack.
If the day with higher temperature is not found, we leave the ans to be the default 0.
 """

def dailyTemperatures(self, temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
      while stack and temperatures[stack[-1]] < t: # 堆棧不為空, 且當前的溫度大於堆棧頂部的溫度
        cur = stack.pop() # 更新current為堆棧頂部
        ans[cur] = i - cur # 更新ans為當前溫度的index-current
      stack.append(i) # 堆棧為空 或是 當前溫度小於堆棧頂部的溫度, 堆棧新增當前溫度的index

    return ans

        
        
# 1249. Minimum Remove to Make Valid Parentheses Medium---------------------------------------
# stack

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ans = ""
        for i in range(len(s)):
            if s[i] != "(" and s[i] != ")": # if s is letter
                ans += s[i]

            elif s[i] == ")": # if s is ")"
                if stack == []: # if there is no unpair-"("
                    continue
                elif stack.pop() == "(": # if there is unpair-"("
                    ans += ")"

            elif s[i] == "(": # if s in "("
                if i == len(s)-1:  # the last can't be "("
                    continue
                else:
                    stack.append("(")
                    ans += "("

        if len(stack) != 0: # if there is unpair-"("
            ans = ans[::-1].replace("(","",len(stack)) # 從後面開始刪除
            ans = ans[::-1] # 再反序

        return ans


s = "lee(t(c)o)de)"
# s = "))(("
s = "())()((("
s = "l)eetcode"
ans = Solution().minRemoveToMakeValid(s=s)
print(ans)

# Smart and faster solution
class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack, cur = [], ''
        for c in s:
            if c == '(':
                stack += [cur]
                cur = ''
            elif c == ')':
                if stack:
                    cur = stack.pop() + '(' + cur + ')' 
            else:
                cur += c
        
        while stack:
            cur = stack.pop() + cur
        
        return cur




# 1037. Valid Boomerang Easy---------------------------------------
# 迴力鏢, 算斜率
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]: # 任兩點重複
            return False
        
        diff_x1 = points[1][0] - points[0][0]
        diff_y1 = points[1][1] - points[0][1]
        try:
            s1 = diff_y1 / diff_x1 # 算點1和點2的斜率, 如果x等於0 (除數不能是0), 斜率slope為None
        except:
            s1 = None
        
        diff_x2 = points[2][0] - points[1][0]
        diff_y2 = points[2][1] - points[1][1]
        try:
            s2 = diff_y2 / diff_x2 # 算點2和點3的斜率, 如果x等於0 (除數不能是0), 斜率slope為None
        except:
            s2 = None

        return False if s1 == s2 else True # 斜率相等 False, 不相等Ture

class Solution:
    def isBoomerang(self, p):
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])
        # diff_x * diff_y != diff_x * diff_y
        # 1-2 * 1-3 != 1-3 * 1-2
        # 1-2 * 1-2 != 1-3 * 1-3
            
points = [[1,1],[2,2],[3,3]] # false
points = [[1,1],[2,3],[3,2]] # true






# 1046. Last Stone Weight Easy---------------------------------------

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            first = max(stones)
            stones.remove(first)
            second = max(stones)
            stones.remove(second)
            if first == second:
                continue
            else:
                diff = first - second
                stones.append(diff)
        return stones[0] if stones != [] else 0
            
        
# 1047. Remove All Adjacent Duplicates In String Easy---------------------------------------

# Time Limit Exceeded
class Solution:
    def removeDuplicates(self, s):
        print(s)

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                delete = s[i]*2
                s = s.replace(delete,"")
                s = self.removeDuplicates(s)
                break
        
        return s
            
                
s = "abbaddggxxseeca"
ans = Solution().removeDuplicates(s=s)
print(ans)


# Time Limit Exceeded
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        deletes = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                delete = s[i]*2
                deletes.append(delete)
        
        if deletes != []:
            for delete in deletes:
                s = s.replace(delete,"")
            s = self.removeDuplicates(s)
        
        return s
            

# Memory Limit Exceeded
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        deletes = ["aa","bb","cc","dd","ee","ff","gg","hh","ii",'jj','kk','ll','mm','nn','oo','pp','qq','rr','ss',
'tt','uu','vv','ww','xx','yy','zz']       
        
        for delete in deletes:
            if delete in s:
                s = s.replace(delete,"")
                s = self.removeDuplicates(s)
        
        
        return s
            
                
# stack and pop !!!!!!!!!!!
class Solution:
    def removeDuplicates(self, s: str) -> str:

        ans = []
        for c in s:
            if ans and ans[-1] == c:
                ans.pop()
            else:
                ans.append(c)
                
        return ''.join(ans)
            
                
s = "abbaddggxxseeca"

        
                

# 1049. Last Stone Weight II  Medium---------------------------------------
# openbook
# 背包問題(Knapsack), 求和問題: 416. Partition Equal Subset Sum
# DP
""" 
題目說兩個石頭遇到之後，重量小的會消失，重量大的剩下兩個石頭的重量之差。
如果倆石頭一樣重，則同時消失。
最後求出所有石頭相遇之後剩下的那一個石頭重量的最小值。
其實簡單來說，就是把這一組石頭的重量附上加減號，求和最小的可能。

例如 2,7,4,1,8,1 總和23
組a 總和11 數字4 7 
組b 總和12 數字2 1 8 1
相差1


例如 31,26,33,21,40 總和151
組a 總和73 數字40 33
組b 總和78 數字31 21 26
相差5



我們可以將石頭分成兩部分（都是正整數），兩部分分別求和，
這兩個和的差值最小的情況即為最優解。

這樣問題就轉化為：是否能找到n個數，他們的和最接近整體和的一半。
進而題目就變成了另外一題LEETCODE 416.Partition Equal Subset Sum。他們的思路完全相同。

解決這類問題的關鍵是求和，
確切的說，是需要求出所有數字能夠組成的和的可能，
然後再從這些和中選出一個最接近目標值的數字（小於等於目標值）即為答案。
 """

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) / 2
        sum_of_subsets = set([0]) # 存放已知相加小於/等於target的數字
        
        for n in stones:
            sum_with_n = [] 
            for i in sum_of_subsets: 
                if i + n <= target:
                    sum_with_n.append(i + n) # 存放"已知不到terget且這次加上n也小於等於target"的數字
            sum_of_subsets.update(sum_with_n)
            
        print(max(sum_of_subsets)) # 最接近target的數字

        return sum(stones) - max(sum_of_subsets)*2
                    
        


# 1051. Height Checker Easy---------------------------------------

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_heights = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != sort_heights[i]:
                ans += 1
        return ans
        



# 953. Verifying an Alien Dictionary Easy---------------------------------------

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index_map = {n: i for i, n in enumerate(order)}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b: # 前面內容一樣, 但是長的排在前
                return False
            for s1, s2 in zip(a, b): # 比每一個單字
                if index_map[s1] < index_map[s2]: # 如果字母順序小的確實在前面, break. 如果相等, 繼續比.
                    break
                elif index_map[s1] > index_map[s2]:
                    return False
        return True
        

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
        
ans = Solution().isAlienSorted(words=words, order=order)
print(ans)





# 961. N-Repeated Element in Size 2N Array Easy---------------------------------------

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(set(nums)) - 1
        for k, c in Counter(nums).items():
            if c == n:
                return k
        

# 36. Valid Sudoku Medium---------------------------------------

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check column
        # a = list(zip(*board)) 可以用zip(*example)來做橫豎交換
        for i in range(9):
            tmp  = []
            for row in board:
                if row[i] != "." and row[i] in tmp:
                    return False
                else:
                    tmp.append(row[i])
                    
        # check row
        for row in board:
            tmp  = []
            for n in row:
                if n != "." and n in tmp:
                    return False
                else:
                    tmp.append(n)
                    
        # check squre            
        index = [0,3,6]
        squres = []
        for i in index:
            for j in index:
                squres.append([i,j])

        for squre in squres:
            grid = []
            for i in range(squre[0],squre[0]+3):
                for j in range(squre[1],squre[1]+3):
                    if board[i][j] != "." and board[i][j] in grid:
                        return False
                    grid.append(board[i][j])
            # print(grid)

        return True
                        
             



# 53. Maximum Subarray Easy---------------------------------------
# time limit Exceeded
# DP
# openbook
class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        sum_list = [nums[0]]
        for i in range(1, len(nums)):
            sum_list.append(sum_list[-1] + nums[i])

        max_sum = max(sum_list)

        for i in range(len(sum_list)-1):
            cur_max = max(sum_list[i+1:]) - sum_list[i]
            if cur_max > max_sum:
                max_sum = cur_max

        return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]
        for n in nums[1:]: # 0被放進去了, 從1開始
            cur_sum = max(n, cur_sum+n) # 是n大, 還是從以前加到n大
            max_sum = max(max_sum, cur_sum) # 是曾經出現過的大, 還是cur有創新高
            
        return max_sum
            


# 541. Reverse String II Easy---------------------------------------

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        if len(s) < k:
            s = s[::-1]
            return s
        elif len(s) < k*2 and len(s) >= k:
            r = s[0:k]
            s = r[::-1] + s[k:]
            return s
          
        elif len(s) >= k*2:
            for i in range(0, len(s), k*2):
                r = s[i:i+k]
                ans += r[::-1] + s[i+k:i+k*2]
            return ans
               
                
        


# 561. Array Partition I Easy---------------------------------------

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return sum(nums[0:-1:2])
        
        ans = 0
        for i in range(0,len(nums),2):
            ans += nums[i]
            
        return ans
        
        


# 2022. Convert 1D Array Into 2D Array Easy---------------------------------------
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        ans = []
        for i in range(0,len(original),n):
            sub_list = []
            for j in range(n):
                sub_list.append(original[i+j])
            ans.append(sub_list)

        return ans        



# 566. Reshape the Matrix Easy---------------------------------------

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat_list = []
        for row in mat:
            for n in row:
                mat_list.append(n)

        if r * c != len(mat_list):
            return mat

        ans = []
        for i in range(0,len(mat_list),c):
            sub_list = []
            for j in range(c):
                sub_list.append(mat_list[i+j])
            ans.append(sub_list)

        return ans


# num_title Easy Medium---------------------------------------
# num_title Easy Medium---------------------------------------




# num_title Easy Medium---------------------------------------
# num_title Easy Medium---------------------------------------
# num_title Easy Medium---------------------------------------
# num_title Easy Medium---------------------------------------
# num_title Easy Medium---------------------------------------
# num_title Easy Medium---------------------------------------
# num_title Easy Medium---------------------------------------
