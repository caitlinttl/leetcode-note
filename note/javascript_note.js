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