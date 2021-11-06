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

# 氣泡排序
# Big O: Time Complexity: O(n^2), Space Complexity: O(1)
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

        
