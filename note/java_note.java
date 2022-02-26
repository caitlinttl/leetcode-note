// class 的名字和文件名字要一樣
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.io.File;
import java.io.IOException;

public class java_note { 
    public static void main(String[] args) {  
    // 如果想要運行此程序，程序中必須要有一個main函數，運行程序時，main函數中的代碼就會被執行。
        System.out.println("Hello World!");
    }

    public static void name_data_type() {
        // pubilc static 是修飾符，決定了該方法的訪問類型

        // public代表是公開的類, attributes, method可以被任何類訪問
        // private就是私有的, 無法被其他類訪問
        // protected 適用於繼承關係的類, attributes, method可以被子類訪問

        // static 修飾符可以讓方法的適用範圍變為"全局"
        // 不需要通過具體的實例（實例是一個類的具體對象）來使用此方法。
        // 如果沒有static修飾符，我們則需要創建實例來調用方法。

        // void則是該方法的返回值的數據類型
        // void代表不返回任何數值
        // 也可以是int, String, boolean 等等數據類型。

        // 封裝Encapsulation
        // - 封裝意味著將數據的細節隱藏起來，僅公開有限的接口接口給用戶。

        // 繼承Inheritance
        // - 把原來的類稱為父類或基類，而派生出來的類稱為子類，子類則會繼承父類的數據和方法。

        // 多態Polymorphism
        // - 指針對不同類型的參數進行相同的操作，根據對象（或類）類型的不同而表現出不同的行為。


        // 抽象Abstraction
        // - 數據抽象的意思是隱藏細節，只暴露最重要的信息給用戶。
        // - 抽象可以通過abstract class 或interface（接口）實現。

        // abstract class
        // - abstract 關鍵字是一個用於類和方法的"修飾符"，
        // 我們無法創建abstract class 類型的實例，這種抽像類只能被繼承。
        // abstract method只能定義在abstract class中，這種方法沒有具體執行內容。
        // 一個抽像類既abstract class可以有抽象方法也可以有正常的方法
        // 一個類繼承了抽像類，那麼此類必須要實現抽像類中定義的抽象方法


        // 接口Interface
        // 一個接口就是完全的抽像類，其中只含有抽象方法，
        // 這些方法中是沒有任何邏輯代碼的。
        // 類的主要作用便是定義一些特定的方法，具體邏輯讓正常的類實現
        // 具體的類必須實現其屬性相對應的特定方法，幫助實現數據的抽象化。
        // 如果要使用接口的方法，那麼具體的類必須實現（implements）其接口。
        // 只要被實現，具體的類必須將接口方法的具體邏輯全部實現

        // 繼承 v.s. 接口
        // "繼承" 之間的關係是is-a，也就意味著子類是父類的一個子集。
        // "接口" 的類和接口之間的關係是has-a，意味著具體類擁有接口的一些功能。





        


        /**
         * 我是
         * 多行
         * 註釋
         */
        
        //  變量的type, 指定後不能更改


        /** 
         * print就是一般的標準輸出，但是"不換行"
         * println和print基本沒什麼差別，最後"會換行"
         * printf是格式化輸出的形式。
        */

    
        //  常量: final
        final int myNum = 15;
    
        // byte -> short -> char -> int -> long -> float -> double
        // 自動類型轉換 (低位轉高位)
    
        char c1 = 'z';
        int i1 = c1; // char自動轉換成int
    
    
        // double -> float -> long -> int -> char -> short -> byte
        // 強制類型轉換 (高位轉低位)
    
        double doubleNum = 9.9;
        int intNum = (int)doubleNum; // 9
    
        
        float floatNum = 5;
        char letter = 'A';
    
        int intNuma = 10;
        double floatNumDouble = 5;
        boolean bool = true;
        
    }


    public static void name_condition() {

        // （?:）
        // 條件運算符（三元運算符）會根據布爾表達式的判斷，來決定將哪個值賦給變量
        int score = 80;
        int reward = (score >= 80) ? 100 : 50;
    
        // instanceof 能夠對實例進行判斷，檢查該實例是否是一個特定的類型（類或接口）
        java_note a = new java_note();
        boolean isMain = a instanceof java_note;
        System.out.println(isMain); // true
        
    }

    public static void name_array() {

        // arrey用尖括號
        int[] numbers = {10, 20, 30, 40};
        String[] names = {"Alice", "David", "Enoch", "Alex"};
        System.out.println(names[0]); // Alice
        System.out.println(names[3]); // Alex
        names[0] = "Daniel"; // 將Alice換成Daniel        
        String[] cars = {"BMW", "Ford", "Porsche", "Ferrari"};
        System.out.println(cars.length); // 4   


        // 二維數組
        int[][] numMatrix = { {1, 2, 3, 4}, {5, 6, 7, 8}};
        int num = numMatrix[0][3]; // 4

    }

    public static void name_String() {
        // String 是一個類
        String message = "hello";
        System.out.println(message);
        System.out.println(message.length());
        System.out.println(message.toUpperCase());
        System.out.println(message.indexOf('e'));
        System.out.println(message.substring(1, 2));
        System.out.println(message.substring(1, message.length()));

        
    }    

    public static void name_Math() {
        /**
         * max(x, y) – 判斷較大的值
         * abs(x) – 得到絕對值
         * sqrt(x) – 平方根
         * random() – 得到一個隨機的在0和1之間的浮點數（不包括1）
         */
        System.out.println(Math.max(2, 20)); // 20
        System.out.println(Math.abs(-25)); // 25
        System.out.println(Math.sqrt(25)); // 5.0
        System.out.println(Math.random()); // 0.52434....
        
    }

    public static void name_If() {
        int score = 70, reward = 0;
        if(score >= 90) {
            reward = score * 2;
        } else if (score >= 80) {
            reward = score * 3 / 2;
        } else if (score >= 60) {
            reward = score;
        } else {
            reward = 0;
        }
        System.out.println("Reward: " + reward); // 70        
    }
    
    enum Membership { NORMAL, SILVER, GOLD, DIAMOND };
    // enum 是 final
    public static void mealCalculation() {
        Membership memberType = Membership.GOLD;
        int mealPrice = 1000, payment = 0;
        if (memberType == Membership.GOLD || memberType == Membership.DIAMOND) {
            payment = mealPrice * 8 / 10;
        } else if (memberType == Membership.SILVER) {
            payment = mealPrice * 9 / 10;
        } else {
            payment = mealPrice;
        }
        System.out.printf("You should pay $%s for the meal.\n", payment);
    }        

    public static void name_switch() {

        char grade = 'A';
        switch (grade) {
            case 'A':
                System.out.println("Great job!");
                break;
            case 'B': 
            case 'C':
                System.out.println("Good job.");
                break;
            case 'D': 
            case 'F': 
                System.out.println("You can do better.");
                break;
            default:
                System.out.println("Unknown grade");
        }        
    }


    public static void name_While() {

        int i = 0;
        while(i < 5) {
            System.out.println(i);
            i++;
        }
        

        // 使用do…while，不管循環條件是否為真，循環至少會被執行一次。
        int j = 0;
        do {
            System.out.println(j);
            j++;
        } while(j < 5);    

    }

    public static void name_For() {

        for (int i = 0; i < 5; i++ ) {
            System.out.println(i);
        }
        
        for (int i = 0; i <= 10; i = i + 2) {
            System.out.println(i);
        }    

        String[] cars = {"Ford", "BMV", "Porsche", "Ferrari"};
        for (String car: cars) {
            System.out.println(car);
        }    
    }


    /**
     * 方法重載Method Overloading 
     * 方法重載可以讓我們使用"相同的方法名"，來處理不同的參數，比如下面這些方法
     */
    public int sum(int num1, int num2) {
        return num1 + num2;
    }
    public double sum(double num1, double num2) {
        return num1 + num2;
    }


    // 常用的類與方法
    // String 字符串類
    // trim() – 將前導或尾隨的空格移除
    // toCharArray() – 轉換成字符數組
    // substring(index, length) – 取一個子串，第一個參數是子串開始的位置，第二個參數是子串結束的指數
    // replace(s1, s2) – 把字符串中的s1變為s2

    public static void name_String_method() {

        String str = "  Hello World    ";
        str = str.trim(); // "Hello World"
        str = str.replace("World", "Enoch"); // "Hello Enoch"
        str = str.substring(6, 11); // "Enoch"
        char[] charArray = str.toCharArray(); // ['E', 'n', 'o', 'c', 'h']        
    }


    // Math 數學運算的類
    // min(num1, num2) – 得到兩個數之間的較小數
    // sqrt(n) – 計算出n的平方根
    // pow(num, n) – 計算出num的n次方
    // floor(float) – 將浮點數變為最近的一個整數

    public static void name_Math_method() {

        double num1 = 14, num2 = 9.345;
        double minNum = Math.min(num1, num2); // 9.345
        minNum = Math.floor(minNum); // 9.0
        minNum = Math.sqrt(minNum); // 3.0
        minNum = Math.pow(minNum, 3); // 27.0        
    }

    // Array 
    // Arrays, Collections, List是經常被使用操作數組的類，這個類在java.util包中，
    // 所以我們想要調用時，必須在文件的最上面加上以下的import導入此類

    // sort() – 將數組排序
    // toString() – 將數組變為已讀的字符串
    // asList – 將數組轉換成列表
    // reverse(array) – 將數組中的元素反轉

    public static void name_Array_method() {

        Integer[] array = {5, 7, 6, 3, 4, 2, 1};
        Arrays.sort(array); 
        System.out.println(Arrays.toString(array)); // {1, 2, 3, 4, 5, 6, 7}
        List<Integer> arrayList = Arrays.asList(array);
        Collections.reverse(arrayList);
        System.out.println(arrayList); // [7, 6, 5, 4, 3, 1]    
    }


    public static void name_try_catch() {

        System.out.println("-----Hello World!-----");
        
        try {
            System.out.println(1/0);
        } catch (ArithmeticException e) {
            System.out.println("An exception occurs.");
        }        

        try {
            // System.out.println(1/0);
            int[] array = new int[]{1, 2};
            System.out.println(array[3]);
        } catch (ArithmeticException e) {
                System.out.println("An exception occurs.");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("An exception occurs2.");

        }

        try {
            // System.out.println(1/0);
            int[] array = new int[]{1, 2};
            System.out.println(array[3]);
            } catch (Exception e) {
                System.out.println(e);
            } finally {
                System.out.println("Runnnn");
            }

            
    }   

    // throws 拋出異常給上一層處理
    public static void badCode() throws ArithmeticException, IndexOutOfBoundsException{
        System.out.println(0 / 1);
        int[] array = new int[]{1, 2};
        System.out.println(array[3]);
    }

    // throw 拋出自定義的異常
    public static void checkAge(int age) {
        if (age < 18) {
            throw new ArithmeticException("Access denied: You must be at least 18 years old.");
        } else {
            System.out.println("Access granted: You are old enough!");
        }    
    }
}