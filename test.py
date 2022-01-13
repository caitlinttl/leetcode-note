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

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2,1] 
nums = [-2,-1]
nums = [5,4,-1,7,8]
nums = [-1,0,-2]
ans = Solution().maxSubArray(nums=nums)
print(ans)