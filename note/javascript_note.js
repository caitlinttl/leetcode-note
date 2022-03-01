var x = 5;
x = "abc"; 
// 需要var了，因為第一行var x已經將x定義為變量了，不需要重複定義。

var x = 1, y = 9;

const PI = 3.14;
PI = 3; // Uncaught TypeError: Assignment to constant variable.
// 一個const變量被賦值了，就不能改變了
// 還要注意到恆定變量的名字最好全是大寫。

var x = 5;
console.log(x); // 5

// 數據類型
var num1 = 34.00;
var num2 = 34;
var bool1 = true;
var bool2 = false;
var str = "Good";

var cars = ["BMW", "Honda", "Ferrari"];
console.log(cars[0]); // BMW
console.log(cars[2]); // Ferrari

var undefined_var; // undefined
var null_var = null; // null

// 邏輯運算符
// &&	和	true && false; // false
// ||	或	true || false; // true
// !	否	!true; // false

var x = true;
var y = false;
true && false; // false

Math.min(2, 3, 4); // 2 
Math.max(8, 13, 1); // 13


var score = 70, reward = 0;
if (score >= 90) {
    reward = score * 2;
} else if (score >= 80) {
    reward = score * 3 / 2;
} else if (score >= 60) {
    reward = score;
} else {
    reward = 0;
}
console.log("Reward: " + reward); // 70


/* 

布爾條件：true
查詢是否相等或不等：age == 18
數值比較：age >= 21
字符串比較：car == “BMW”
多個條件判斷：score >= 60 && score <= 80

 */

/* 
==（相等）	比较两个操作数的值是否相等
!=（不想等）	比较两个操作数的值是否不相等
===（全等）	比较两个操作数的值是否相等，同时检测它们的"類型"是否相同
!==（不全等）	比较两个操作数的值是否不相等，同时检测它们的"類型"是否不相同
*/


// includes
var cars = ["audi", "bmw", "subaru", "toyota"];
if (cars.includes("bmw")) {
    console.log("I have BMW!");
}

// Checking multiple conditions
var age_1 = 22;
var age_2 = 18;
if (age_1 >= 21 && age_2 >= 21) { // and
    console.log("You can both drink.");
} else {
    console.log("You can't drink together.");
}
if (age_1 >= 21 || age_1 >= 21) { //or
    console.log("one of you can drink.");
}

// switch
// switch語句，它會根據不同條件執行不同的代碼塊
// switch語句中的變量類型可以是：boolean、number或者string
/* 
如果出現break 關鍵詞，那麼switch語句就會終止
break 關鍵詞不是必須的，如果沒有的話，
程序就會繼續執行下一個case語句，直到出現break為止。
如果所有的case都不滿足，那麼switch就會執行default中的語句。
 */

var grade = "A";
switch (grade) {
    case "A":
        console.log("Great job!");
        break;
    case "B": 
    case "C":
        console.log("Good job.");
        break;
    case "D": 
    case "F": 
        console.log("You can do better.");
        break;
    default:
        console.log("Unknown grade");
}


// while
var num = 0;
while (num < 10) {
  console.log(num);
  num++;
}


// do…while語句
// 這個循環裡的代碼"至少會被執行一次"，然後再根據循環條件判斷是否需要再次繼續：
var num = 0;
do {
  console.log(num); // 至少執行一次
  num++;
}
while (num < 10);


// for
// 遍歷array
for (var i = 0; i < 5; i++) {
    console.log(i);
  }

fruits = ["Banana", "Orange", "Apple", "Mango"];

length = fruits.length;
for (i = 0; i < length; i++) {
console.log(fruits[i]);
}

for (const s of fruits) {
    console.log(s);
  }

fruits.forEach(function (item, index) {
console.log(item, index);
});


// continue, while
var sum = 0;
while(true) {
    var num = Number(window.prompt("Enter a number: "));
    if (num % 2 == 0) {
        sum += num;
        console.log("sum = " + sum);
        continue;
    }
    var response = window.prompt("Do you want to continue?(Y/N)");
    if(response.toLowerCase()[0] == 'n') {
        break;
    }
}

while(true){
    var num1 = Number(window.prompt("Enter num1: "))
    var num2 = Number(window.prompt("Enter num2: "))
    if (num1 > num2) {
        break
    }
    for (i=num1; i<=num2; i++) {
        if (i % 2 != 0) {
            console.log(i)
        }
    }
}


// function
function printMultiplication(num1, num2) {
    console.log(num1 * num2);
  }

printMultiplication(5, 6); // 30
printMultiplication(2, 3); // 6


function evenNumberOperator(num) {
    if (isEven(num)) { 
        return addFive(num);
    } else {
        return num;
    }
}

/* 
includes  是否包含
indexOf   查index


 */
var cars = ["BMW", "AUDI", "VOLVO"];
console.log(cars.includes("BMW")); // true


// 箭頭函數
// 這種函數的語法比正常函數更簡潔
// 箭頭函數會自動返回執行內容
// 對於邏輯簡單的代碼，我們可以直接使用箭頭函數實現。

hello = function() {
    return "Hello World!";
}

hello = () => {
    return "Hello World!";
}

hello = () => "Hello World";


concatenateTwoWords = (w1, w2) => w1 + " " + w2;
console.log(concatenateTwoWords("Hello", "World")); // Hello World

var func = x => x * x;
console.log(func(2))
// concise body syntax, implied "return"
// 沒有括號可以不寫return

var func = (x, y) => { return x + y; }; 
// with block body, explicit "return" needed
// 有括號要寫return



// 變數作用域 var vs. let
// var 全局，變量都是全局變量：
// let 局部，變量的生存週期不是全局的，而是被限制在一個"區塊"內

/* 
var 裡面有 var >> OK
var 裡面有 let >> OK
let 裡面有 let >> OK
let 裡面有 var >> ERROR
*/


// Callback 回調/乎回
// 一個程式執行完再去執行另一個程式
// 1、讓函式成為另一個函式的參數
// 2、讓函式控制參數函式的執行時機

/* 
程式當執行到setTimeout時，會先跳過該程式，把執行的順序優先讓給下一個函式。這樣的好處是其他的函式不會因為需要等待而影響執行的時間。講簡單一點，不要讓整個網頁因為一個函式都因為等待而變慢，這樣使用者才不會覺的網頁很慢或很卡。 */
/* 
在真正的網站開發中回調是非常重要的，比如在一個function從別的網站下載數據的時候，我們希望特定函數必須在這個數據下載完畢後才能執行，那麼我們就需要使用回調，不讓函數的執行順序就因為需求回應的時間不同而亂套了。
 */


function first(callback) {
    setTimeout(function() {
        console.log(1);
        callback();
    }, 500); 
}

function second(){
    console.log(2)
}

first(second);

function doHomework(subject, callback) {
    alert(`Starting my ${subject} homework.`);
    callback();
  }
  
doHomework('math', function() {
alert('Finished my homework');
});


function sumArray(array1, array2) {
    var newArray = [];
    for (var i = 0; i < array1.length; i++) {
        newArray.push(array1[i] + array2[i]);
    }
    return newArray;
}

var array1 = [1, 5, 8, 9];
var array2 = [2, 4, 8, 1];
var newArray = sumArray(array1, array2); // [3, 9, 16, 10]
console.log(newArray)




// 面對對象編程
// 每個對象擁有自己的屬性和方法

var person = {
    firstName: "David",
    lastName: "Wang", 
    age: 23
};

console.log(person.firstName); // David
console.log(person.lastName); // Wang
console.log(person.age); // 23

var dog = {
    name: "Doudou", // 屬性
    greet: function() { //方法
        console.log(this.name + ": " + "Wang Wang!"); // this 對象本身自己
    }
};

dog.greet(); // Doudou: Wang Wang!


var dog = new Object();
dog.name = "Doudou";
dog.greet = function() {
    console.log(this.name + ": " + "Wang Wang!");
};
dog.greet(); // Doudou: Wang Wang!




function greetFunction() {
    console.log(`Hi, I am ${this.first_name} ${this.last_name}.`);
}

function Person(first_name, last_name) { // 首字母要大寫
    this.first_name = first_name;
    this.last_name = last_name;
    this.greet = greetFunction;  
};

var person = new Person("David", "Wang"); // 基於Person 創建新的對象
person.greet(); // Hi, I am David Wang.

// 瀏覽器對象

console.log('width: ' + window.innerWidth + ', height: ' + window.innerHeight);

console.log('appName = ' + navigator.appName);
console.log('appVersion = ' + navigator.appVersion);
console.log('language = ' + navigator.language);
console.log('platform = ' + navigator.platform);
console.log('userAgent = ' + navigator.userAgent);

window.history.back();
window.location.href;


// ------------------------------

function printFunction() {
    console.log(`Brand: ${this.brand} Model: ${this.model} Year: ${this.year}`);
}

function Car(brand, model='xxx', year='0') {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.print = printFunction;
}

var car = new Car("Audi");
var car = new Car("Audi", "apple", "1234");
car.print();

// ------------------------------

function Car(brand) {
    this.brand = brand;
    this.model = "xxx";
    this.year = 0;
    this.set_model = function(model) {
        this.model = model;
    }; 
    this.set_year = function(year) {
        this.year = year;
    };
    this.get_info = function() {
        console.log(`Brand: ${this.brand}, Model: ${this.model}, Year: ${this.year}`);
    };
};

var new_car = new Car("Subaru");
new_car.set_model("WRX");
new_car.set_year(2014);
new_car.get_info();


/* 
JavaScript可以通過以下4種方式來控制HTML：

使用id來找HTML元素
使用tag名字來找HTML元素
使用class名字來找HTML元素
使用HTML object collections來找HTML元素 

*/


// 使用id 名字尋找HTML 元素：
var head1 = document.getElementById("h1");
head1.innerHTML="New Heading";


// 使用tab 名字找HTML 元素：
var paragraphs = document.getElementsByTagName("p");
for (const p of paragraphs) {
   p.innerHTML = 'New Paragraph';
};

// 使用class 名字來找HTML 元素：
var p2 = document.getElementsByClassName("c1");
for (const obj of p2) {
   obj.style.background = "pink";
}

// 使用CSS Selectors 來找HTML 元素：
var x = document.querySelector("p.c1");
x.style.background = "yellow";

// 使用HTML Object Collections 尋找HTML 元素：
console.log(document.links.length);

document.anchors
document.forms
document.images
document.links
document.scripts

var jsonText = '{ "employees" : [' +
'{ "name":"Kevin" , "age":"29" },' +
'{ "name":"David" , "age":"31" },' +
'{ "name":"Peter" , "age":"27" } ]}';

// AJAX (Asynchronous JavaScript and XML)
/* AJAX 是Asynchronous JavaScript and XML 的縮寫，代表了一系列用來構建網站程序的技術。
通過AJAX 技術，網絡程序能從客戶端發出並獲取服務器的數據，
*** 在不更新當前網站的情況下，自動重新加載其展示內容。 ***
*/



// array 操作
var fruits = ['Apple', 'Banana'];

// 在陣列中尋找項目的索引indexOf
var pos = fruits.indexOf('Banana'); // 1

// 長度length
console.log(fruits.length); // 2

// 取得值[]
var first = fruits[0]; // Apple

// 增加項目到末端push
var newLength = fruits.push('Orange'); // ["Apple", "Banana", "Orange"]

// 疊代iteration forEach
fruits.forEach(function (item, index) {
    console.log(item, index);
    });
fruits.forEach(function(item, index, array) {
    console.log(item, index);
  });
  // Apple 0
  // Banana 1


// 移除陣列末端項目pop
var last = fruits.pop(); // 移除 (最末端的) Orange
// ["Apple", "Banana"];

// 移除陣列前端項目shift
var first = fruits.shift(); // 移除 (最前端的) Apple
// ["Banana"];

// 加入項目至陣列前端unshift
var newLength = fruits.unshift('Strawberry') // 加到陣列前端
// ["Strawberry", "Banana"];

// 移除指定索引位置的項目splice
var removedItem = fruits.splice(position, n); // 移除 position 起的 n 個項目
// ["Strawberry", "Mango"]

// 複製陣列slice
var shallowCopy = fruits.slice(); // 這就是複製陣列的方式
// ["Strawberry", "Mango"]


document.write('hello!<br>');

var m = prompt('how many?','10000');
if(m<30000){
    m = Number(m);
    alert(m+1);
}else if(m>10000000){
    alert('有錢人!');
}else{
    alert('NO!');
}

var n = 0;
while(n<=10){
    n++;
    document.write(n+'<br>');
    console.log(n);
}

初始區塊; 判斷; 迴圈區塊
for(var i=1; i<=10; i++){
    document.write(i+'<br>');
    console.log(i);
}

var n = 0;
while(n<=100){
    if(n==20){
        break;
    }
    n++
    console.log(n)
}



function test(n1,n2){
    // alert(n1+n2);
    return n1+n2
}

var a = test(1,4);
document.write(a);

function test(n1,n2){
    // alert(n1+n2);
    n1 = String(n1)
    n2 = String(n2)
    return n1+n2
}

var a = test('rrr','ddd');
document.write(a);


var x = 3; //全域變數
function test(){
    var y = 5; //區域變數
    document.write(y);
}

test()




var point=new Object();
// 建立物件的成員
point.x = 3; //屬性
point.y = 4;
point.getPosition = function(){ //方法
    document.write(this.x + "," + this.y + '<br>');
    document.write('2222')
    return 5555
};

console.log(point.getPosition());



// ----------物件設計----------
// 物件設計
var player=new Object();
player.name = "Amy";
player.hp = 100
player.fight = function(){
    this.hp = this.hp-2;
    
};
player.reset = function(){
    this.hp++;

};
player.report = function(){
    document.write(this.name + ": " + this.hp);
};

// 物件使用
player.fight();
player.reset();
player.report();




// ----------建構式物件----------
function Player(name, hp = 100){ //建構物件的函式, 第一個字大寫
    // this 代表新建的空白物件
    this.name = name;
    this.hp = hp;
    this.fight = function(){
        this.hp -= 2;
    }
    this.reset = function(){
        this.hp += 1;
    }
    this.report = function(){
        document.write(this.name + ": " + this.hp + "<br>");
    }
} 

var player = new Player("Bee", 200);
player.fight();
player.reset();
player.report();

var player2 = new Player("Cat");
player2.fight();
player2.reset();
player2.report();



// =====================================================================================================
// *****Array 操作
// =====================================================================================================

Array.isArray(obj)                      // 檢驗是否為陣列
const arrCopy = [...arr]                // 複製陣列（copy array）@ airbnb 4.3
const nodes = [...arrayLike]            // 將 array-like（例如 NodeList） 轉成 array @ airbnb 4.4

/**
 * 建立陣列
 **/
let arr = [element0, element1, ..., elementN]        /* Good */
let arr = new Array(element0, element1[, ...[, elementN]])  /* Bad  */
let arr = new Array(arrayLength)

/**
 * 原陣列不會被改變 (non-mutating) 而是回傳新陣列
**/
arr.at(-1)        // 取出陣列的最後一個元素，可以用來替換 arr[arr.length-1] 的寫法
arr.map( callback<element> )                  // 用來將陣列中的元素做轉換（computed），搭配 return
arr.forEach( callback<item, index, array> )   // 用來疊代陣列中的元素，並執行動作，不需搭配 return
arr.slice(begin, end)                         // 用來擷取陣列中的部分元素（不包含 end）
arr.filter( callback<item, index, array> )    // 若 callback return 為 true 時則保留該元素
arr.reduce( callback<accumulator, currentValue, currentIndex, array>, initialValue )  // 搭配 return ，return 的內容會進到 accumulator，最後回傳 accumulator
arr.join('<str>')                            // 將陣列以 <str> 連接成字串，預設是","

// 根據 callback 的規則篩選，需在 callback 中搭配 return 使用
arr.some( callback<item, index, array> )      // 檢驗陣列中是否有符合該 callback 規則的元素，有的話回傳 true
arr.every( callback<item, index, array> )     // 檢驗陣列中所有元素是否都符合 callback 規則，有的話回傳 true
arr.find( callback<item, index, array> )      // 檢驗陣列中是否有符合該 callback 規則的元素，有的話回傳第一個找到的元素值
arr.findIndex( callback<item, index, array> ) // 檢驗陣列中是否有符合該 callback 規則的元素，有的話回傳第一個找到的 index

// 根據 target 篩選
arr.includes(target, fromIndex)               // 檢驗陣列中是否包含 target 這個 element，有的話回傳 true
arr.indexOf( target, fromIndex )              // 返回找到該元素的第一個 index 值，若找不到則回傳 -1

/**
 * 原陣列會被改變(mutation method)
**/
arr.pop()                                     // 刪除最後一個元素
arr.push()                                    // 將元素塞入陣列中
arr.shift()                                   // 刪除陣列中第一個元素
arr.unshift()                                 // 將元素插入到陣列中第一個
arr.splice(start, deleteCount, newItem)       // 用來移除陣列中的部分元素，並可補入新元素
arr.sort(compareFunction)                     // 根據 compareFunction 來將陣列重新排序
arr.concat(value1, [value2], ...)             // 把陣列連接在一起



判斷式否為陣列（型別判斷）
keywords: Array.isArray()
Array.isArray([]); // true
Array.isArray([1]); // true
Array.isArray(new Array()); // true

Array.isArray(); // false
Array.isArray({}); // false
Array.isArray(null); // false
Array.isArray(undefined); // false


將 array-like 的 Node List 轉成 Array
// rails/activestorage/app/javascript/activestorage/helpers.js
function toArray(value) {
  if (Array.isArray(value)) {
    return value;
  } else if (Array.from) {
    return Array.from(value);
  } else {
    return [].slice.call(value);
  }
}


從陣列中隨機抽取一個元素（sample element in array）
var rand = myArray[Math.floor(Math.random() * myArray.length)];

/**
 * 建立一個長度為 length ，且所有內容均為 'element' 的陣列
 * create an array with same element in given length
 **/
 Array(_length_).fill(_element_);
 Array(10).fill('ele');
 // [ 'ele', 'ele', 'ele', 'ele', 'ele', 'ele', 'ele', 'ele', 'ele', 'ele' ]


 Array(5)               // [empty × 5]
[...Array(5)]          // [undefined, undefined, undefined, undefined, undefined]
[...Array(5).keys()]   // [0, 1, 2, 3, 4]

Array(5).keys()         // Array Iterator {}


去除陣列中重複的元素（keep unique element）
let arr = ['aaron', 'po', 'aaron', 'po', 'chung'];
let arrKeepUniqueElements = [...new Set(arr)];


篩選出最小值
let minX = arr.reduce((pre, cur) => {
  return pre.x < cur.x ? pre.x : cur.x;
});


陣列的解構賦值（Array Destructing）
let [a, b, c] = [1, 2, 3];
console.log(a, b, c); // 1, 2, 3

let destructing_array = function () {
    let allPeople = ['Aaron', 'John', 'Andy', 'Hat', 'Candy'];
    let [a, b, c, ...d] = allPeople;
    console.log(a, b, c, d); // Aaron John Andy ["Hat", "Candy"]
  };

  let [a, b, c = 4, d = 'Hello'] = [1, 2, 3];
console.log(a, b, c, d); // 1, 2, 3, "Hello"


let arr = ['Taipei', 'Taiwan', 'Aaron'];
console.log(arr.length); //  取得陣列元素數目


/**
 * 會改變原本的陣列內容
 **/
let arr_pop = arr.pop(); //  用來刪除最後一個元素
console.log(arr); //  ["Taipei", "Taiwan"]
console.log(arr_pop); //  'Aaron'

let arr_push = arr.push('Apple'); //  用來將元素塞入陣列中
console.log(arr); //  ["Taipei", "Taiwan", "Apple"]
console.log(arr_push); // 3

let arr_shift = arr.shift(); //  刪除第一個元素
console.log(arr); //  ["Taiwan", "Apple"]
console.log(arr_shift); //  "Taipei"



/**
 * 不會改變原本的陣列內容
 **/
let arr_map = arr.map((item) => item + 's'); //  將陣列中的每個元素執行某函式，但不改變原來的 arr
console.log(arr); //  ["Taipei", "Taiwan", "Apple"]
console.log(arr_map); //  ["Taipeis", "Taiwans", "Apples"]

// 使用 Array.prototype.slice 來避免改變原陣列

// 為陣列添加元素
const addElement = (originArray) => {
    return [...originArray, 0];
  };
  
  // 移除陣列內的元素
  const removeElement = (originArray, index) => {
    return [...originArray.slice(0, index), ...originArray.slice(index + 1)];
  };
  
  // 改變陣列內的元素
  const modifyElement = (originArray, index) => {
    return [...originArray.slice(0, index), originArray[index] + 1, ...originArray.slice(index + 1)];
  };


// 連結陣列 joining arrays
const odd = [1, 3, 5];
const arr_concat = [2, 4, 6].concat(odd);
const arr_spread = [2, 4, 6, ...odd]; // [2, 4, 6, 1, 3, 5]

// 陣列插值 insert array anywhere
const arr_insert = [2, 4, ...odd, 6]; // [2, 4, 1, 3, 5, 6]

// 複製陣列 cloning array, copy array, clone array
const arr = [1, 2, 3, 4];
const arr2 = [...arr]; // [1, 2, 3, 4]


/**
 *   var new_array = arr.map(callback<item, index, array>)
 *   需要使用到陣列，並回傳回原陣列時，所以在 callback 中會有 return
 **/
 var numbers = [1, 5, 10, 15];
 var roots = numbers.map(function (x) {
   return x * 2;
 });
 // roots is now [2, 10, 20, 30]
 // numbers is still [1, 5, 10, 15]


 /**
 *  arr.forEach(callback<currentValue, index, array> [, thisArg]);
 *  需要使用到陣列，但不需要回傳陣列時使用（根據這個陣列自己做一些事）
 **/

let people = [
    { name: 'Aaron', country: 'Taiwan' },
    { name: 'Jack', country: 'USA' },
    { name: 'Johnson', country: 'Korea' },
  ];
  
  people.forEach((person) => {
    console.log(`${person.name} lives in ${person.country}`);
  });
  
  //    特殊簡寫
  let users = ['Aaron', 'Jack', 'Johnson'];
  function getUserName(username) {
    console.log(username);
  }
  
  users.forEach(getUserName);
  
  /* 上面這行是下面這段的簡寫
  users.forEach( user =>{
      getUserName(user)
  })
  */


擷取陣列中的部分元素

/**
 *   arr.slice(),
 *   arr.slice(begin)
 *   arr.slice(begin, end)
 *   slice() 方法將陣列的一部分淺拷貝,
 *   回傳從 begin 開始到 end 結束（不包括 end）新陣列。
 *   原始陣列不會被修改。
 **/

let arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
arr.slice(0, 3); // [0,1,2]
arr.slice(3, 7); // [3,4,5,6]

// 最後一個是 -1
arr.slice(-3, -1); // [8,9]
arr.slice(-5, -3); // [6,7]
arr.slice(-3, -5); // []

// 如果要擷取到最後一個
arr.slice(-5, arr.length); // [6,7,8,9,0]



移除陣列元素（並放入新陣列元素） 
注意事項：splice( ) 的用法會改變原陣列結構，且原本的 arr 和 arrSplice 會輸出不同內容。

/**
 *  array.splice(start)
 *  array.splice(start, deleteCount)
 *  array.splice(start, deleteCount, item1, item2, ...)
 *
 *  deleteCount：要移除的陣列個數，省略表示 arr.length - start
 *  item1, item2：可用來從 start 添加陣列
 **/

 arr = [1, 3, 5, 6];
 arr_splice = arr.splice(2, 1); //  表示把第 2 個元素從陣列中移除
 console.log(arr); //  保留下來的元素，回傳 [1, 3, 6]
 console.log(arr_splice); //  被移除掉的元素，回傳 [5]
 arr_splice = arr.splice(2, 1, 'new'); //  把第 2 個元素從陣列移除，並放進新元素"new"



排序
/**
 *    arr.sort(compareFunction)
 *    會改變原陣列
 **/

 arr = [4, 6, 3, 3, 6, 8, 12];

 function compareNumbers(a, b) {
   // console.log(a, b)
   return a - b; // 由小排到大
   // return b - a   // 由大排到小
 }
 arr.sort(compareNumbers);
 console.log(arr); //    [3, 3, 4, 6, 6, 8, 12]


/**
 * 根據屬性值排序，但是屬性值不能有空的情況
 **/

var arr = [
{ name: 'Edward', value: 21 },
{ name: 'Sharpe', value: 37 },
];

function compareObj(a, b) {
return a.value - b.value;
}
arr.sort(compareObj);
console.log(arr);


/**
 *  arr.filter(callback<element, index, array> [, thisArg])
 *  若回傳值為true則將當前的元素保留; 若是false，則刪除該元素。
 **/

//  把所有小於 10 的資料都移除
function isBigEnough(value) {
    return value >= 10;
  }
  var filtered = [12, 5, 8, 130, 44].filter(isBigEnough); // filtered is [12, 130, 44]


/**
 *   arr.indexOf(searchElement[, fromIndex = 0])
 *   indexOf() 方法返回在數組中可以找到給定元素的第一個索引，如果不存在，則返回-1
 **/



/**
 * 用來檢驗陣列中是否包含某規則的元素
 * 會針對陣列中的每個元素去執行 some 裡面的 callback ，如果有 true 就停止，沒有就到最後回傳 false
 * arr.some(callback<element, index, array> [, thisArg] )
 */

 function isBiggerThan10(element, index, array) {
    return element > 10;
  }
  
  [2, 5, 8, 1, 4].some(isBiggerThan10); // false
  [12, 5, 8, 1, 4].some(isBiggerThan10); // true


  /**
 * 建議要給起始值
 * arr.reduce( callback<accumulator, currentValue, currentIndex, array>, initialValue )
 * 搭配 return 使用，return 的內容會傳到 accumulator
 **/

// 基本使用
let arr = [0, 1, 2, 3, 4];

let arrAfterReduce = arr.reduce((accumulator, item, currentIndex) => {
  return accumulator + item; // return 的值會進入 accumulator
}, 0);

console.log('afterReduce ' + arrAfterReduce); // 10

// 可以用來篩選陣列小值
let minX = arr.reduce((pre, cur) => {
  return pre.x < cur.x ? pre.x : cur.x;
});


/* 取得陣列中放在物件裡的值 */
let arr = [{ name: 'A' }, { name: 'B' }, { name: 'C' }];

let sum = arr.reduce((acc, cur, i, arr) => {
  /* 使用 push */
  acc.push(cur.name); // 回傳陣列長度
  return acc; // 原陣列改變

  /* 使用 concat */
  // return acc.concat(cur.name)    // 回傳連結後的陣列
}, []);

console.log(sum); // [ 'A', 'B', 'C' ]

/**
 * 用來將陣列連接起來
 * arr.concat(value1 [, value2])
 * 和 push 有一個差異是在 push 會改變原本的陣列，
 * 但是 concat 不會改變原本的陣列
 **/

 let arr = [1, 2, 3];
 let arrAppend = [4, 5, 6];
 arr.concat(7, arrAppend); // [1, 2, 3, 7, 4, 5, 6]，arr 不會改變

fill
 建立一個長度為 length ，且所有內容均為 'element' 的陣列（Create an array with the same element）

 /**
 * Array(<length>).fill(<element>)
 **/
Array(3).fill(4); // [4, 4, 4]


// good
const arr = [
    [0, 1],
    [2, 3],
    [4, 5],
  ];
  
  const objectInArray = [
    {
      id: 1,
    },
    {
      id: 2,
    },
  ];
  
  const numberInArray = [1, 2];



// =====================================================================================================
// *****Map 操作
// =====================================================================================================

/* 
Map 物件是簡單的 key-value 配對，物件（Object）和 Map 很相似，但是有以下幾點差別：

Map 裡面的 key 是唯一的，如果 set 到重複的 key，則舊的 value 會被覆蓋。
Map 中的 keys 會根據被添加資料的時間而有順序性，但 Object 沒有順序性。
Object 的鍵（key）只能是 字串（Strings）或 Symbols，而 Map 的鍵可以是任何值，包含物件、函式或原始型別（primitive type）。
若要取得 Map 的大小非常容易，只需要取得 size 屬性即可；而 Object 的大小必須手動決定。
當需要經常增添刪減屬性時，使用 Map 的效能會比 Object 來得好。
*/


ES6 中如果希望「陣列（Array）」的元素不會重複，可以使用 Set；如果是希望物件（Object）的鍵不會重複，則可以使用 Map。

// 建立 Map
let myMap = new Map(); // 建立空的 Map
let myMap = new Map([
  [1, 'one'],
  [2, 'two'],
]); // 建立 Map 時直接代入內容

let keyString = 'a string',
  keyObj = {},
  keyFunc = function () {};

// 透過 .set(key, value) 來在 Map 中添加屬性
myMap.set(keyString, 'value associated with string');
myMap.set(keyObj, 'value associated with object');
myMap.set(keyFunc, 'value associated with function');

// 方法
myMap.has(keyString); // true，透過 .has 判斷該 Map 中是否有某一屬性
myMap.size; //  3，透過 .size 來取得 Map 內的屬性數目
myMap.get(keyString); // 使用 .get(key) 可取得屬性的內容
myMap.delete(keyString); // 刪除 Map 中的某個屬性，成功刪除回傳 true，否則 false
myMap.clear(); // 清空整個 Map


myMap.keys(); // 取得 Map 的所有 keys，回傳 Iterable 的物件
myMap.values(); // 取得 Map 的所有 values，回傳 Iterable 的物件
myMap.entires(); // 取得 Map 的所有內容，回傳 Iterable 的物件


// 透過 for...of 可以列舉所有 Map 中的內容
for (let [key, value] of myMap) {
    console.log(`The value of ${key} in Map is ${value}`);
  }
  
  for (let [key, value] of myMap.entries()) {
    console.log(key + ' = ' + value);
  }
  
  myMap.forEach(function (value, key) {
    console.log(key + ' = ' + value);
  });
  
  // 取得 Map 的 key
  for (let key of myMap.keys()) {
    console.log(key);
  }
  
  // 取得 Map 的所有 values
  for (let value of myMap.values()) {
    console.log(value);
  }


  let students = {
    Aaron: { age: '29', country: 'Taiwan' },
    Jack: { age: '26', country: 'USA' },
    Johnson: { age: '32', country: 'Korea' },
  };
  
  const studentMap = new Map(Object.entries(students));
  const cloneMap = new Map(studentMap);
  
  cloneMap.get('Aaron'); // { age: '29', country: 'Taiwan' }
  studentMap === cloneMap; // false. Useful for shallow comparison


// Map 的合併（Merge）
  var first = new Map([
    [1, 'one'],
    [2, 'two'],
    [3, 'three'],
  ]);
  
  var second = new Map([
    [1, 'uno'],
    [2, 'dos'],
  ]);
  
  // 合併兩個 Map 時，後面的 Key 會覆蓋調前面的
  // 透過 Spread operator 可以將 Map 轉換成陣列
  var merged = new Map([...first, ...second]);
  
  console.log(merged.get(1)); // uno
  console.log(merged.get(2)); // dos
  console.log(merged.get(3)); // three



// Map 也可以和陣列相合併
// Merge maps with an array. The last repeated key wins.
var merged = new Map([...first, ...second, [1, 'foo']]);

console.log(merged.get(1)); // foo
console.log(merged.get(2)); // dos
console.log(merged.get(3)); // three


let students = {
    Aaron: { age: '29', country: 'Taiwan' },
    Jack: { age: '26', country: 'USA' },
    Johnson: { age: '32', country: 'Korea' },
  };
  
  const studentMap = new Map(Object.entries(students));
  
  // 透過 for...of 可以列舉所有 Map 中的內容
  for (let [key, value] of studentMap) {
    const { age, country } = value;
    console.log(`${key} is ${age} year's old, and lives in ${country}`);
  }
  
  //  檢驗某個鍵是否存在
  studentMap.has('Aaron');
  
  console.log(studentMap.get('Jack')); // 取得 Map 的屬性內容，Object { age: '26', country: 'USA' }
  studentMap.delete('Johnson'); // 刪除 Map 中的某個屬性
  studentMap.clear(); // 清空整個 Map
  
  console.log(studentMap.size); // 看看 Map 中有多少內容


//   將 Map 轉成 Array
const theMap = new Map([
    [1, 'one'],
    [2, 'two'],
    [3, 'three'],
  ]);
  
  const theArray = [...theMap.entries()]; // [[1, 'one'], [2, 'two'], [3, 'three']]
  const arrayOfMapKeys = [...theMap.keys()]; // [1, 2, 3]
  const arrayOfMapValues = [...theMap.values()]; // ["one", "two", "three"]



// 使用 Map 製作 HashTable
// object 也可以使用
const arr = ['apple', 'apple', 'banana', 'banana', 'cat', 'dog', 'fat', 'fat', 'fat', 'fat'];

const hashTable = new Map();

arr.forEach((item) => {
  if (hashTable.has(item)) {
    hashTable.set(item, hashTable.get(item) + 1);
  } else {
    hashTable.set(item, 1);
  }
});

// Map { 'apple' => 2, 'banana' => 2, 'cat' => 1, 'dog' => 1, 'fat' => 4 }
console.log(hashTable);


// =====================================================================================================
// *****String 操作
// =====================================================================================================

.length
charAt()
charCodeAt()
concat()
indexOf()
lastIndexOf()
match()
replace()
search()
slice()
split()
substr()
substring()
toLowerCase()
toUpperCase()

trim() 
//移除字串起始及結尾處的空白字元。 本文中的空白字元指所有空格字元（如：空格、欄標、無間斷空格等等）及換行字元（如：換行、回車等等）。

// =====================================================================================================
// *****Array 操作
// =====================================================================================================

arr.at(-1)        // 取出陣列的最後一個元素，可以用來替換 arr[arr.length-1] 的寫法
arr.map( callback<element> )                  // 用來將陣列中的元素做轉換（computed），搭配 return
arr.forEach( callback<item, index, array> )   // 用來疊代陣列中的元素，並執行動作，不需搭配 return
arr.slice(begin, end)                         // 用來擷取陣列中的部分元素（不包含 end）
arr.filter( callback<item, index, array> )    // 若 callback return 為 true 時則保留該元素
arr.reduce( callback<accumulator, currentValue, currentIndex, array>, initialValue )  // 搭配 return ，return 的內容會進到 accumulator，最後回傳 accumulator
arr.join('<str>')                            // 將陣列以 <str> 連接成字串，預設是","

// 根據 callback 的規則篩選，需在 callback 中搭配 return 使用
arr.some( callback<item, index, array> )      // 檢驗陣列中是否有符合該 callback 規則的元素，有的話回傳 true
arr.every( callback<item, index, array> )     // 檢驗陣列中所有元素是否都符合 callback 規則，有的話回傳 true
arr.find( callback<item, index, array> )      // 檢驗陣列中是否有符合該 callback 規則的元素，有的話回傳第一個找到的元素值
arr.findIndex( callback<item, index, array> ) // 檢驗陣列中是否有符合該 callback 規則的元素，有的話回傳第一個找到的 index

// 根據 target 篩選
arr.includes(target, fromIndex)               // 檢驗陣列中是否包含 target 這個 element，有的話回傳 true
arr.indexOf( target, fromIndex )              // 返回找到該元素的第一個 index 值，若找不到則回傳 -1

/**
 * 原陣列會被改變(mutation method)
**/
arr.pop()                                     // 刪除最後一個元素
arr.push()                                    // 將元素塞入陣列中
arr.shift()                                   // 刪除陣列中第一個元素
arr.unshift()                                 // 將元素插入到陣列中第一個
arr.splice(start, deleteCount, newItem)       // 用來移除陣列中的部分元素，並可補入新元素
arr.sort(compareFunction)                     // 根據 compareFunction 來將陣列重新排序
arr.concat(value1, [value2], ...)             // 把陣列連接在一起



// =====================================================================================================
// *****Map 操作
// =====================================================================================================

// 透過 .set(key, value) 來在 Map 中添加屬性
myMap.set(keyString, 'value associated with string');
myMap.set(keyObj, 'value associated with object');
myMap.set(keyFunc, 'value associated with function');

// 方法
myMap.has(keyString); // true，透過 .has 判斷該 Map 中是否有某一屬性
myMap.size; //  3，透過 .size 來取得 Map 內的屬性數目
myMap.get(keyString); // 使用 .get(key) 可取得屬性的內容
myMap.delete(keyString); // 刪除 Map 中的某個屬性，成功刪除回傳 true，否則 false
myMap.clear(); // 清空整個 Map


myMap.keys(); // 取得 Map 的所有 keys，回傳 Iterable 的物件
myMap.values(); // 取得 Map 的所有 values，回傳 Iterable 的物件
myMap.entires(); // 取得 Map 的所有內容，回傳 Iterable 的物件


