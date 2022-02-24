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


# Tree
# https://turingplanet.org/2020/03/17/%e6%a0%91tree-%e4%ba%8c%e5%88%86%e6%9f%a5%e6%89%be%e6%a0%91binary-search-tree%e3%80%8c%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84%e5%92%8c%e7%ae%97%e6%b3%957%e3%80%8d/
# Binary search tree 二分查找樹 (BST)
# Tree traversal 遍歷
# - 前序遍歷 Preorder Traversal 自己左右 (先訪問自己, 然後訪問左孩子, 再訪問右孩子) Top -> Bottom, left -> right
# - 中序遍歷 Inorder Traversal 左自己右 (先訪問左孩子, 再訪問自己, 再訪問右孩子) left -> node -> right
# - 後序遍歷 Postorder Traversal 左右自己 (先訪問左右孩子, 再訪問自己)  Bottom -> Top, left -> right

""" 
Tree

頭(root)
尾(leaf)
node之間相連的線，叫做edge
Height(到尾): 節點到尾節點之間 edge的數量
Depth(到頭): 節點到root之間 edge的數量

樹的分類:
- 二叉樹（Binary Tree）：每個節點最多含有兩個子樹，上面的圖標就是二叉樹。
- 排序二叉樹（Binary Search Tree）：在此樹中，每個節點的分數比左子樹上的每個節點都大，比所有右子樹上的節點都小。
- 完全二叉樹（Complete Binary Tree）：假設一個完整的二叉樹深度（深度）為d（d > 1），除了第d層外，其他層的不同數量均已達到完整的結果，且第d層所有節點從左方向右樹就是這樣排列，這樣的二叉樹完全是二叉樹。
- 滿二叉樹（Full Binary Tee）：在滿二叉樹中，每個不是尾節點的節點有兩個子節點。
- 平衡二叉樹（AVL Tree）：任何節點的兩顆子樹的高度差不大於1的二叉樹。
- B樹（B-Tree）：B樹和平衡二樹一樣，它是一種多叉樹（一個插節點的節點數量可以超過二）。
- 紅黑樹（Red—Black Tree）：是一種自平衡二叉樹。

BST裡面不能存在相同value的節點

"""


# 94. Binary Tree Inorder Traversal Easy---------------------------------------
# Tree
# inorder 左 自己 右
# https://blog.csdn.net/fuxuemingzhu/article/details/79294461
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(root):
            if root == None:
                return None

            if root.left != None:     # 左
                inorder(root.left)

            ans.append(root.val)      # 自己

            if root.right != None:    # 右
                inorder(root.right)
        
        inorder(root)
        return ans

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(root):
            if root == None:
                return None

            ans.append(root.val)      # 自己
                
            if root.left != None:     # 左
                inorder(root.left)
            
            if root.right != None:    # 右
                inorder(root.right)
        
        inorder(root)
        return ans

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(root):
            if root == None:
                return None
            if root.left != None:     # 左
                inorder(root.left)
            
            if root.right != None:    # 右
                inorder(root.right)
            
            ans.append(root.val)      # 自己
        
        inorder(root)
        return ans

        
"""

root = [1,null,2,3]
TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}
inorder: [1,3,2]
preorder: [1,2,3]
postorder: [3,2,1]

"""


# 101. Symmetric Tree Easy---------------------------------------
# 判斷樹是否對稱

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None: # root 為空, return True
            return True
        else:
            return self.isSymmetricTree(root.left, root.right) #root 不為空, 往下看, 傳入root的左子樹和右子樹
        
    def isSymmetricTree(self, left, right):
        if left == None or right == None: # 左右子樹有其中一個為空
            return True if left == right else False # 如果左右子樹都為空為True, 如果一個空一個不空為False
        if left.val != right.val: #左右子樹都不為空, 那比左右子樹的值, 值如果不同為False
            return False
        # 左右子樹的值相同, 繼續往下比, recusion自己, 傳入邊緣情況與中間情況
        edge = self.isSymmetricTree(left.left, right.right) # 傳入邊緣(左的左 和 右的右比)
        center = self.isSymmetricTree(left.right, right.left) # 中間情況(左的右 和 右的左比)
        if edge == True and center == True: # 如果邊緣和中間都是True, 則為True
            return True
        
TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: TreeNode{val: 3, left: None, right: None}}, right: TreeNode{val: 2, left: None, right: TreeNode{val: 3, left: None, right: None}}}
            
root = [1,2,2,null,3,null,3]
        


# 104. Maximum Depth of Binary Tree Easy---------------------------------------

# 問的是tree的層數, 所以要加一(加自己)
# DFS
""" 
-DFS思路
- 利用pre-order (node, L, R)
- 先看node是不是空 是空的話 那return 0 (base case)
- 不是的話 那就往左往右看下去找到最深的pth因為雨分樹有雨條路 所以要比較
左邊右邊找出比較深的那條路 找到之後 也要把自己算進去所以pth的深度在加1
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))




# 108. Convert Sorted Array to Binary Search Tree Easy---------------------------------------
""" 
因此採用二元搜尋來產生二元搜索樹,
首先將該陣列的中間值作為整個樹的根結點,
採用遞迴分別建立左右節點 

https://desolve.medium.com/%E5%BE%9Eleetcode%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-35-bst-3-b1f225f39aa3

"""


""" 

1. 檢查陣列是否是空的或者null，是的話直接回傳
2. 呼叫一個用來遞迴建立BST的函式，這邊命名成getNode()
3. getNode會輸入陣列以及當下的左右邊界(nums, l, r)
(一開始l = 0, r = N-1, N是nums的總數)
4. 每次先檢查左右邊界是否黃金交叉(表示已經完成了，可以回傳null)
5. 讓mid = l加r的一半，直接建立一個root節點
6. root節點的左節點就應該是呼叫getNode(nums, l, mid-1)得到的結果
7. root節點的右節點則會是getNode(nums, mid+1, r)得到的結果
8. 回傳root
我們可以看到每次會抓中間值產生一個節點，再利用已排序的特性，
繼續進入遞迴往下將左邊和右邊的節點處理完畢。
思考它的執行流程，應該會發現總體而言我們會先一路來到最左邊的節點，
再回頭建立每個遞迴函式的右邊節點；
也就是說，程式執行的優先順序是先往深處的方向走而非先將這一層的狀況處理完，這種模式我們稱之為深度優先搜尋(Depth-First Search, DFS)；
 """

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == None or len(nums) == 0:
            return None
        return self.getNode(nums, 0, len(nums) -1)

    def getNode(self, nums: List[int], left:int, right:int):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.getNode(nums, left, mid-1)
        root.right = self.getNode(nums, mid+1, right)
        return root



""" 

PriorityQueue 優先對列
Heap 堆
https://turingplanet.org/2020/03/07/%e4%bc%98%e5%85%88%e9%98%9f%e5%88%97-priorityqueue/

幫助我們以最快的速度O(1)獲取優先級最高的元素。

PriorityQueue 優先對列
push：插入一個新的元素  O(n)
pop：將優先級最高的元素彈出（刪除） O(1)
peek：查看優先級最高的值 O(1)


堆Heap
堆（Heap）是一種特殊的平衡二叉樹，堆中的節點滿足以下的條件：一個節點的父節點優先級比自己高，而自己的子節點優先級比自己底。優先級可以根據數值的大小來決定。最常見的堆有以下兩種類型：

最大堆（Max Heap）：最大堆中根節點數值最大，所有父節點的數值比各自的子節點數值大。
最小堆（Min Heap）：根節點數值最小， 父節點數值比其子節點數值小。
add: 將新元素插入堆
poll: 將根節點（數值最大的元素）刪除
peek: 獲取根節點的數值


 """


 """ 

 Graph 圖
https://turingplanet.org/2020/04/02/%e5%9b%begraph%e3%80%8c%e7%ae%97%e6%b3%95%e5%92%8c%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%849%e3%80%8d/


1. 向圖（Undirected Graph）：和其他無直接連接的圖）。
2. 有向圖（DirectGraph）：有向圖的連線是有方向的。
3. 權重圖（Weighted Graph）：在重圖中，每條線都有各自的權重。

 DFS
 BFS

 圖的遍歷（Graph Traversal）
 深度優先搜索（Depth-First Search）
 廣度優先搜索（Breadth-First Search）
 
  """

# 頂點 vertice
# 相連線 edge