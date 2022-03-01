// 796. Rotate String Easy---------------------------------------
/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
 var rotateString = function(s, goal) {
    return s.length == goal.length && (s+s).includes(goal)
};


// 1. Two Sum Easy---------------------------------------

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

// use map
var twoSum = function(nums, target) {

    var ans = []
    var seen = new Map()
    for (i = 0; i < nums.length; i++) {
        var diff = target -  nums[i]
        if (seen.has(diff)) {
            ans.push(seen.get(diff), i)
            return ans
        }
        seen.set(nums[i], i)
    }

};



console.log("-----test js-----")
var nums = [2,7,11,15]
var target = 9
console.log(twoSum(nums,target))


// 27. Remove Element Easy---------------------------------------
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
 var removeElement = function(nums, val) {
    
    // filter 不會改變原陣列!!
    var nums = nums.filter(function(value) {
        return value != val 
    })   
    console.log(nums)
    return nums.length


    function removeVal(value) {
        return value != val
    }
   return nums.filter(removeVal).length  

};

 var removeElement = function(nums, val) {
    
    while (nums.includes(val)) {
        nums.splice(nums.indexOf(val), 1)
        // splice 會改變原陣列
    }
    return nums.length

};

var removeElement = function(nums, val) {
    let pos;
    while((pos = nums.indexOf(val)) !== -1) {
        nums.splice(pos,1);
    }
    return nums.length;

};


// 28. Implement strStr() Easy---------------------------------------

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
 var strStr = function(haystack, needle) {
    if (needle == "") {
        return 0
    }
    if (!haystack.includes(needle)){
        return -1
    } else {
        return haystack.indexOf(needle)
    }
   
};



// 14. Longest Common Prefix Easy---------------------------------------

/**
 * @param {string[]} strs
 * @return {string}
 */
// Time Complexity: O(M*N), M = length of shortest word, N = length of given array
// Space Complexity: O(1)
 var longestCommonPrefix = function(strs) {
    if (!strs.length) return "";
    let ans = "";
    for (var i = 0; i < strs[0].length; i++) {
        for (var j = 0; j < strs.length -1; j++) {
            if (strs[j][i] !== strs[j+1][i]) {
                return ans;
            }
        }
        ans += strs[0][i];
    }
    return ans
    
};


var longestCommonPrefix = function(strs) {
    if (!strs.length) return '';
    
    for (let i = 0; i < strs[0].length; i++) {
        for (let s of strs) {
            if (s[i] !== strs[0][i]) return s.slice(0, i);
        }
    }
    return strs[0]
    
};


var strs = ["flower","flow","flight"]
console.log(longestCommonPrefix(strs))


// num_title Easy Medium---------------------------------------
// num_title Easy Medium---------------------------------------


// num_title Easy Medium---------------------------------------
// num_title Easy Medium---------------------------------------
// num_title Easy Medium---------------------------------------

