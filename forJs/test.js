/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
 var reverseString = function(s) {
    return s.reverse()
    
};


console.log("-----test js-----")
var start = new Date().getTime(); 

// ------------------------------

var strs = ["flower","flow","flight"]
var strs = ["ab", "a"]
var val = 2
var s = "leetcode";
var s = ["h","e","l","l","o"];
var needle = "ll";

console.log(reverseString(s))

// ------------------------------

var end = new Date().getTime();    
console.log("Elapse of time: " + (end - start) +  " ms")