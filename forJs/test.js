/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    for (i = 0; i < nums.length; i++) {
        for (j = i+1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target ) {
                return [i, j]
            }
        }
    }
};

console.log("-----test js-----")
var nums = [2,7,11,15]
var target = 9
console.log(twoSum(nums,target))