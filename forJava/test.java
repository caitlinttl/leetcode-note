import java.util.ArrayList;
import java.util.Arrays;
import java.util.Arrays;
import java.util.List;
import java.util.HashMap;

public class test {

    public static void main(String[] args) {
        System.out.println("-----test java-----");
        test run = new test();
        long startTime = System.currentTimeMillis();

        // ------------------------------

        int[] nums = {0,1,2,2,3,0,4,2};
        int val = 2;
        String r = "aacd";
        String m = "aabc";
        String needle = "a";
        // String[] strs = {"ab", "a"};
        String[] strs = {"flower","flow","flight"};
        char[] s = {'h','e','l','l','o'};
        
        boolean ans = run.reverseString(s);
        // System.out.println(ans);
        System.out.print(run.reverseString(s));
        // System.out.println(Arrays.toString(ans));
        
        // ------------------------------

        long endTime = System.currentTimeMillis();
        System.out.println("Elapse of time: " + (endTime - startTime) +  " ms");
    }
    

    public boolean reverseString(char[] s) {
        for (int i = 0; i < s.length/2; i++) {
            char tmp = s[i];
            s[i] = s[s.length - 1 - i];
            s[s.length -1 -i] = tmp;
        }

        
        return true;
        
    }




    // ----------------------------------------------------------

}
