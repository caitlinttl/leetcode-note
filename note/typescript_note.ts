// -------------基本類型-------------

let str: string = 'haha';
let num: number = 1000;
let boo: boolean = true;
let n: null = null;
let un: undefined = undefined;
let test: any; // 任何類型

let str1: string; // 事先宣告
let str2 = 'hehe';  // 可以不用宣告類型, ts會自動判斷
let aa = undefined; // aa is any

// 陣列
let arr: string[] = ["a", "b"];
let arr2: number[] = [1, 2];
let arr3: string[][] = [["a", "b"], ["cc", "dd"]];

// 元組
let tuple: [number, string, boolean] = [1, "2", true];
let tuple2 = [1, "2", true]; // 會自動推導類型
let tuple3: [string, string][] = [['a', 'b']]

// -------------Enum 枚舉-------------
enum LiveState {
    SUCCESS = 0,
    FAIL = -1,
    LIVE = 1
}

const st = LiveState.SUCCESS; 


// -------------Union-------------
let aaa: number | string // 定義成不同type
aaa = 1000;
aaa = '1000';

// -------------type-------------
type A = number | string
let a1: A;
a1 = 111
a1 = '111'

// -------------interface-------------
interface user {
    name: string;
    age: number;
}

// -------------object-------------
// type和interface的區別:
// type不能擴充，而interface可以擴充
// interface可以被class繼承

type Card = {
    name: string;
    desc: string;
}
const obj: Card = {
    name: 'sdfsd',
    desc: '12121'
}

interface Card2 {
    name: string;
    desc: string;
}

interface Card2 {
    age?: number
}
// 會結合兩個Card2


const obj2: Card2 = {
    name: 'sdfsd',
    desc: '12121',
    // age: 35
    // age: 因為有加"?": number | undefined, 應用的時候, 即使沒有定義也不會報錯
}


// -------------function-------------
// 參數
// 加"?"代表可以接受undefined

function hello (a: string, b: string) {
    return a + b
}

function hello2 (a: string, b: string): number {
    console.log(a, b)
    return 999
}

function hello3 (a: number, b: boolean, c: string): number {
    return a
}

// undefined
function hello4 (name: string, age?: number){
    // A required parameter cannot follow an optional parameter
    if (age === undefined) return;   // 這行很重要, 避免掉undefined的情況
    test2(age)

}

function test2 (a: number) {
    console.log(a)
}

// 箭頭函式
const func = () => {
    
}
const func1 = () => {
    return 1
}


// ------------ 斷言 unknown-------------
// 透過人工的方式讓ts知道這個變數應該要被推導成什麼類型
// 用來接後斷API, data = xxxx as Type

// type Data = {
//     "userId": 1,
//     "id": 1,
//     "title": "delectus aut autem",
//     "completed": false
// }
type Data = {
    userId: number,
    id: number,
    title: string,
    completed: boolean
}

async function getData() {
    const res = await fetch('https://jsonplaceholder.typicode.com/todos/1')
    const data = await res.json() as Data
    
}

const data1: Data = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
}

type Beta = {
    name: string
}

// 假設data是動態的, 先轉換成unknowm
const beta = data1 as unknown as Beta


// -------------Class-------------
// public
// private: 只有在class可以訪問到, 繼承的時候訪問不到, new的時候訪問不到
// protected: 在繼承的時候可以用super訪問到, new的時候訪問不到
// (僅在開發ts時有此特性,編譯成js還是都能看到)

class Live {
    roomName: string // 預設為public
    private id: string
    protected name: string

    constructor (roomName1: string, id1: string, name1: string) {
        this.roomName = roomName1
        this.id = id1
        this.name = name1
    }
    start () {
        this.id
        this.name
        this.roomName
    }
}

class carLive extends Live {
    constructor (roomName1: string, id1: string, name1: string) {
        super(roomName1, id1, name1)
    }

    start() {
        super.name
        super.roomName
        super.id // Property 'id' is private and only accessible within class 'Live'
    }
}

const live = new Live('1', '000001', 'aaa')
// 私有變數與保護變數無法訪問(僅在開發ts時有此特性)
console.log(live.id) // Property 'id' is private and only accessible within class 'Live'.
console.log(live.name) // Property 'name' is protected and only accessible within class 'Live' and its subclasses.

const carlive = new carLive('1', '000001', 'aaa')
console.log(live.id) // Property 'id' is private and only accessible within class 'Live'
console.log(live.name) // Property 'name' is protected and only accessible within class 'Live' and its subclasses.

class Live2 {
    #name // 私有變數, 真正的私有變數, js也看不見的
    constructor (name: string) {
        this.#name = name
    }
}

const live2 = new Live2("apple")
live2.#name
// Property '#name' is not accessible outside class 'Live2' because it has a private identifier.

export interface carProp {
    name: string
    age: number
    start: () => void
}

class Car implements carProp {
    // implement的不能為private或protected
    name: string 
    age: number

    constructor(name: string, age: number) {
        this.name = name
        this.age = age
    }

    start() {}
}


// -------------泛型Generics-------------
// 在調用的時候才決定類型
function print<T> (data: T) {
    console.log(data)
}

print<number>(999)
print<number>("apple") // Argument of type 'string' is not assignable to parameter of type 'number'.
print<string>("apple")

class Print<T> {
    data: T
    constructor(d: T) {
        this.data = d
    }
}

const print2 = new Print<string>("apple")
const print3 = new Print<number>(999)


// -------------utility-------------
// 工具
// https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type

// Record: 指定的key, 指定的value
interface CatInfo {
    age: number;
    breed: string;
  }
   
  type CatName = "miffy" | "boris" | "mordred";
   
  // key, value
  const cats: Record<CatName, CatInfo> = {
    miffy: { age: 10, breed: "Persian" },
    boris: { age: 5, breed: "Maine Coon" },
    mordred: { age: 16, breed: "British Shorthair" },
  };
   
  cats.boris;

  const obj1: Record<string, boolean> = {
    a: true,
    b: "aaa", // Type 'string' is not assignable to type 'boolean'.

  }


// Pick: 從現有的interface裡面挑選要用到的type, 建立成新的type

interface Todo {
    title: string;
    description: string;
    completed: boolean;
  }
   
  type TodoPreview = Pick<Todo, "title" | "completed">;
   
  const todo: TodoPreview = {
    title: "Clean room",
    completed: false,
  };
   
  todo;


// Omit: 從現有的interface裡面刪掉不要的type, 建立成新的type
// omit為刪去的意思

interface Todo {
    title: string;
    description: string;
    completed: boolean;
    createdAt: number;
  }
   
  type TodoPreview2 = Omit<Todo, "description">;
   
  const todo2: TodoPreview2 = {
    title: "Clean room",
    completed: false,
    createdAt: 1615544252770,
  };
   
  todo2;
      
  type TodoInfo = Omit<Todo, "completed" | "createdAt">;
   
  const todoInfo: TodoInfo = {
    title: "Pick up kids",
    description: "Kindergarten closes at 5pm",
  };
   
  todoInfo;


// -------------Type-------------





