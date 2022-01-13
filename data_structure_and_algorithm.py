#  binarySearch
#  TC: O(log n)
#  SC: O(1)
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


# BigO
# TC (time complexity)
# SC (space complexity)
""" 
常數階O(1)
對數階O(logN)
線性階O(n)
線性對數階O(nlogN)
平方階O(n²)
立方階O(n³)
K次方階O(n^k)
指數階(2^n)
階乘O(n!)
 """



 # Sort Algorithm
# https://www.gushiciku.cn/pl/pHjz/zh-tw
# https://turingplanet.org/2020/02/11/%e6%8e%92%e5%ba%8f%e7%ae%97%e6%b3%95%e3%80%90%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84%e5%92%8c%e7%ae%97%e6%b3%953%e3%80%91/
 # 912. Sort an Array Medium---------------------------------------
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
從頭到尾依次掃描未排序序列，將掃描到的每個元素插入有序序列的適當位置。 
（如果待插入的元素與有序序列中的某個元素相等，則將待插入元素插入到相等元素的後面。 ）
 """
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1 
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1 
        arr[preIndex+1] = current
    return arr

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

""" 
LinkedList
https://turingplanet.org/2020/02/22/%e9%93%be%e8%a1%a8-list%e3%80%90%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84%e5%92%8c%e7%ae%97%e6%b3%953%e3%80%91/

array 需要存放在連續的空間
linkedList 不用確定空間長度，不夠的時候，直接申請新的節點，幫助插入。所以鍊錶可以更靈活地進行內存分配。

每個節點有一個數據域，儲存著節點的
- 數值
- 指針，指向下一個節點。
 
鍊錶的基本操作
每種數據結構都有其對應的操作，而鍊錶包含以下基本操作：

插入：將一個新元素插入鍊錶的任意位置。
刪除：將一個元素從鍊錶中刪除。
查找（遍歷）：查找一個特定的元素。
更新：更新一個節點上的元素。

ListNode:
  self.val = val
  self.next = next
  self.prev = prev
  
  
  0x1: {val: 100, next: 0x100, prev: ???}
  0x2: {......}
  ....
  0x100: {val: 101, next: ??, prev: 0x1}

"""

# List會占用全部的記憶體去貯存資料
# nodeList不需要, 他會用箭頭(next, prev)去做指向, 會多占用一個記憶體去存next(and prev)的資料
# LinkedList 缺陷
# - 不知道長度
# - 要訪問特定位置, 一定要從頭一步一步開始走
# 解決方法:
# 遍歷一次linked List紀錄他的長度n, 然後從頭目開始走n/2步找到終點
# TC: O(n+n/2) = O(n)



# 雙指針 (Two Pointers)
""" 
Linked list 找中間節點

兩個指針指向Linked list節點, 而不是index
兩個指針必定"同向"而行

1. 一個快一個慢, 距離隔開多少
2. 兩個指針移動速度

"""

head: Optional[ListNode] = [1,2,3,4,5]
cur = head
cur = ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
cur.val # 1

# 876. Middle of the Linked List
# 遍歷一次計算全部長度, 遍歷第二次到長度的一半
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur != None:
            length += 1
            cur = cur.next # 走一步
        cur = head

        i = 0
        while i < length//2: # *要取整數!!!
            cur = cur.next
            i += 1
        return cur

# 用雙指針的方式, 一快一慢
# 慢的一次走一步, 快的一次走兩步
# 奇數的情況(fast下一步是None), 返回slow
# 偶數的情況(fast下一步非None)因為有兩個中心, 返回slow.next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next # 走一步的意思
            fast = fast.next.next # 走兩步的意思
            
        return slow if fast.next == None else slow.next


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


# Stack堆棧 and Queue對列
# ====================================
# Stack 後進先出 (如垃圾桶) last in first out
""" 
入棧（Push）：將一個元素放入棧，用來加入數據。
出棧（Pop）：將一個元素彈出棧，用來刪除數據。
Peek：查看最頂部的元素。
isEmpty：查看棧是否為空。

不管是用數組還是鍊錶來實現棧，我們都"只要處理頭節點top"，所以"棧的所有操作都為O(1)"。
"""

# Queue 先進先出 (如隧道排隊) first in first out
""" 
入隊（enqueue）：增加一個新的元素
出隊（dequeue）：刪除一個元素
peek – 查看隊列最前端的元素
isFull – 查看隊列是否滿了
isEmpty – 查看隊列是否為空

"""

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



# 503. Next Greater Element II Medium---------------------------------------
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


# 1047. Remove All Adjacent Duplicates In String Easy---------------------------------------
# openbook
# stack and pop
class Solution:
    def removeDuplicates(self, s: str) -> str:

        ans = []
        for c in s:
            if ans and ans[-1] == c:
                ans.pop()
            else:
                ans.append(c)
                
        return ''.join(ans)




# HashTable哈希表 (Dict)
# https://turingplanet.org/2020/03/08/%e5%93%88%e5%b8%8c%e8%a1%a8-hash-table%e3%80%8c%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84%e5%92%8c%e7%ae%97%e6%b3%956%e3%80%8d/

""" 
不管是數組還是鍊錶，如果我們想要尋找一個特定的數值，時間複雜度都為O(n)。
在哈希表中，不管是尋找、刪除、增加一個新元素，時間複雜度都是O(1)。

哈希表以鍵值的方式來存儲元素，
也就是說每個數據都是以鍵值（key，value）的方式存儲的，
關鍵字（key）是不可重複的，而值是對應於鍵的。
我們可以把哈希表簡單理解為一本字典，
每個鍵（key）是一個單詞，而每個單詞都有自己對應的解釋，也就是值（value）。
 """


""" 
array 尋址容易, 插入/刪除困難
linkedList 尋址困難, 插入/刪除容易
hash 結合array和linkedListL: 拉鍊法, 由一堆linkedList組成的array

 """


""" 
哈希表使用哈希函數（Hash Function）將鍵（key）轉換成一個哈希值（整形數字），
然後將該數組對數組長度取餘，
取餘得到的數字就當做數組的下標，然後將其鍵值對添加到對應的鍊錶中。
尋找一個鍵所對應的值時，我們也是使用哈希函數將鍵轉換為對應的數組下標，並在其鍊錶中定位到該關鍵字所對應的數值。


以下哈希表支持的操作：
get(K key)：通過特定的關鍵字拿到其所對應的值
add(Key key, Value value)：將一對新的鍵值對加入哈希表
remove(Key key)：通過關鍵字，刪除哈希表中的鍵值對
getSize()：當前鍵值對的數量
isEmpty()：查看哈希表是否為空

 """

# 1. Two Sum
# HashMap (dict)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            if target-nums[i] in num_map: # target-nums[i]是要尋找的目標(值)
                return [num_map[target-nums[i]], i] # 回傳 map裡面目標值的index, 和當前index
            else:
                num_map[nums[i]] = i # key是num的值, i是nums的index





