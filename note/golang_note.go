package main // main代表可執行的程式

import "fmt"

// coding => Build => Run
// Build: go build fileName
// Run: hello.exe
// Run: go run hello.go

func main() { // 程式的進入點
	fmt.Println("Hello Golang") // string
	fmt.Println('H')            // rune
	fmt.Println('h')            //print line (換行)
	fmt.Print('h')              //print 不換行

	// -------------------------------------------------
	// Data Type: int/float64/string/bool/rune
	// rune 字元 ex: 'a' 表達單一字符, 背後實際存放整數, 'a'會打印出整數97

	var x int
	x = 5
	fmt.Println(x)

	var f float64 = 3.1415
	fmt.Println(f)
	var b bool = true
	fmt.Println(b)

	// 使用 := 宣告，表示之前沒有進行宣告過。
	// =為賦值, :=為宣告並賦值
	aa := "ssss"
	bb := 23423
	fmt.Println(aa, bb)

	// -------------------------------------------------
	// In and Out
	var x int
	var y int
	// fmt.Println("input 1")
	// fmt.Scanln(&x) // &變數名稱: 取得變數的指標
	// fmt.Println("input 2")
	// fmt.Scanln(&y)
	fmt.Println("input 1 2, 用空格隔開")
	fmt.Scanln(&x, &y) // &變數名稱: 取得變數的指標
	fmt.Println(x * y)

	// -------------------------------------------------
	// 運算
	// 算術運算: +, -, *, /
	// 指定運算: =, +=, -=, *=, /=
	// 單元運算: ++, --
	// 比較運算: >, <, >=, <=, ==
	// 邏輯運算: !, &&, ||

	var r = false && false
	fmt.Println(r) // false

	// -------------------------------------------------
	// if
	var a int = 3
	if a == 2 {
		fmt.Println("yes")
	} else {
		fmt.Println("no")
	}

	// -------------------------------------------------
	// for
	// break continue

	var i int = 1
	for i < 50 {
		// fmt.Println(i)
		i++
	}

	var j int
	var result int
	for j = 0; j <= 50; j++ {
		result += j
	}
	fmt.Println(result)

	// -------------------------------------------------
	// func and return
	func main() {
		fmt.Println("Hello Golang")
		test("apple")
		add(4, 6)
		var x int = add(5, 10)
		fmt.Println(x)
		var a, b int = add2()
		fmt.Println(a + b)
	}
	
	func test(msg string) {
		fmt.Println(msg)
	}
	
	// 單一回傳值
	func add(n1 int, n2 int) int { 
		var result int = n1 + n2
		// fmt.Println(result)
		return result
	}
	
	// 多回傳值
	func add2() (int, int) { 
		return 10, 20
	}	

	// -------------------------------------------------
	// 指標 pointer 用來儲存資料的記憶體位置
	// 建立資料變數 > 取得記憶體位址
	// 存放到指標變數 > 反解指標變數

	// 1. 建立存放資料的變數
	// 2. 取得記憶體位址: &變數名稱
	// 3. 存放到指標變數(注意指標型態): *資料型態
	// 4. 反解指標變數: *指標變數名稱

	var x int = 3
	fmt.Println(&x) // 取得記憶體位址: &變數名稱
	// 0xc00000a158
	var xPtr *int = &x // 指標資料型態: *資料型態
	fmt.Println(xPtr)
	// 0xc00000a158
	var a int = *&x    // 反解運算: *指標變數名稱
	fmt.Println(a)     // 3
	fmt.Println(&a)    // 0xc00000a190
	fmt.Println(*xPtr) // 3
	fmt.Println(&xPtr) // 0xc0000a8020


	// -------------------------------------------------
	// 指標參數 pass by Pointer (v.s. pass by value)
	// pass by value: 不會改變原記憶體位址存放的值
	// pass by Pointer: 會改變原記憶體位址存放的值, 因為傳遞的"是記憶體位址"

	// --- pass by value ---
	func main() {
		fmt.Println("Hello Golang")
		var x int = 10
		add(x)
		fmt.Println(x) // 10 ==> 不會改變原記憶體位址存放的值
	}
	
	func add(x int) {
		x += 10
		fmt.Println(x) // 20
	}	

	// --- pass by Pointer ---
	func main() {
		fmt.Println("Hello Golang")
		var x int = 10
		var xPtr *int = &x
		add(xPtr)
		// add(&x)
		fmt.Println(x) // 20 ==> 會改變原記憶體位址存放的值
	}
	
	func add(xPtr *int) {
		*xPtr += 10
		fmt.Println(*xPtr) // 20 
	}

	// -------------------------------------------------
	// 結構Struc: 存放其他資料欄位的容器
	// 定義結構 > 實體化結構

	type car struct {
		year int
		name string
	}

	var smallCar car = car{2000, "aaa"}
	var bigCar car = car{year: 2024, name: "bbb"}
	fmt.Println(smallCar, bigCar)
	fmt.Println(smallCar.name)
	fmt.Println(bigCar.year)
	bigCar.year = 2030
	fmt.Println(bigCar.year)

	// -------------------------------------------------
	// Array

		var arr [4]int
	fmt.Println(arr[0]) // default: 0
	fmt.Println(arr[1]) // default: 0

	arr[0] = 5
	fmt.Println(arr[0]) // 5

	var arr2 [4]int = [4]int{5, 6, 7, 8}
	fmt.Println(arr2)
	fmt.Println(len(arr2))
	var i int
	for i = 0; i < len(arr2); i++ {
		fmt.Println(arr2[i])
	}


	// -------------------------------------------------
	使用 := 宣告，表示之前沒有進行宣告過。
	這是在 go 中最常使用的變數宣告的方式，因為它很簡潔。

	但因為在 package scope 的變數都是以 keyword 作為開頭，因此不能使用縮寫的方式定義變數（foo := bar），只能在 function 中使用，具有區域性（local variable）

	// 第一種宣告方式（最常用）：short declaration
	func main() {
		foo := "Hello"
		bar := 100

	// 也可以簡寫成
	foo, bar := "Hello", 100
	}

	// 等同於
	func main() {
		var foo string
		foo = "Hello"
	}


	// 第二種宣告方式：variable declaration
	使用時機主要是：

	當你不知道變數的起始值
	需要在 package scope 宣告變數
	當為了程式的閱讀性，將變數組織在一起時
	!!留意：在 package scope 宣告的變數會一直保存在記憶體中，直到程式結束才被釋放，因此應該減少在 package scopes 宣告變數


	// 第二種宣告方式，在 main 外面宣告（全域變數），並在 main 內賦值
	var foo string
	var bar int

	// 可以簡寫成
	var (
		foo string
		bar int
	)

	function main() {
	foo = "Hello"
		bar = 100
	}

	!!不建議把變數宣告在全域環境

	// 第三種宣告方式
	// 第三種宣告方式，直接賦值
	var (
		foo string = "Hello"
		bar int = 100
	)







}
