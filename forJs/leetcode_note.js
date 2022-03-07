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


// 58. Length of Last Word Easy---------------------------------------
/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLastWord = function(s) {
    var s = s.trim()
    var s = s.split(" ")
    console.log(s[s.length -1])
    // return s[s.length -1].length
    return s.at(-1).length
    // 取出陣列最後一個元素
    
};


// 387. First Unique Character in a String Easy---------------------------------------

/**
 * @param {string} s
 * @return {number}
 */
// Time Limit Exceeded !!
 var firstUniqChar = function(s) {
    var s_array = s.split('')
    var s_arrat_set = new Set(s_array)
    for (i = 0; i < s_array.length; i++) {
        var count  = s_array.filter(j => j === s_array[i]).length
        console.log(s_array[i] + ': ' + count)
        if (count === 1) {
            return i
        }
    }
    return -1
    
};

// Pass but too slow
 var firstUniqChar = function(s) {
    var s_array = s.split('')
    var s_arrat_set = new Set(s_array)
    console.log(s_arrat_set.size)
    console.log(s_arrat_set.keys())

    for (key of s_arrat_set.keys()) {
        var count  = s_array.filter(j => j === key).length
        if (count === 1) {
            return s.indexOf(key)
        }
    }
    return -1


    var ans = s_arrat_set.forEach(function (value, key) {
        var count  = s_array.filter(j => j === key).length
        console.log(key + ': ' + count)
    })

    
};

// smart solution !!
 var firstUniqChar = function(s) {

    for (var i = 0; i < s.length; i++) {
        // 條件一: 此字母第一次出現的index為i, 意思是: 這個字母是第一次出現。
        // 條件二: 此字母在index i+1 之後沒有再出現(index=-1), 意思是: 這個字母在這次之後, 就沒有再出現。
        // 同時符合: 第一次出現，且沒有再出現，即是答案。
        if (s.indexOf(s[i]) === i && s.indexOf(s[i], i + 1) === -1) {
            return i;
        }
    }
    return -1
    
};


// 860. Lemonade Change Easy---------------------------------------

/**
 * @param {number[]} bills
 * @return {boolean}
 */
 var lemonadeChange = function(bills) {
    var n5 = 0
    var n10 = 0
    for (var bill of bills) {
        if (bill == 5) {
            n5 += 1;
        } else if (bill == 10) {
            n5 -= 1;
            n10 += 1;
        } else if (bill == 20) {
            if (n10 == 0) {
                n5 -= 3;
            } else {
                n10 -= 1;
                n5 -= 1;
            }
        }
        if (n5 < 0 || n10 < 0) {
        // if (n5 < 0 ) {
            return false;
        }
    }
    return true;
};


// num_title Easy Medium---------------------------------------
// num_title Easy Medium---------------------------------------

// num_title Easy Medium---------------------------------------
// num_title Easy Medium---------------------------------------
// num_title Easy Medium---------------------------------------

