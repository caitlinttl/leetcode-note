var rotateString = function(s, goal) {
    return s.length == goal.length && (s+s).includes(goal)
};

console.log("-----test js-----")
console.log(rotateString("sss","sss"))