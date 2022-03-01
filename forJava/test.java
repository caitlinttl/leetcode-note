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
        String haystack = "hello";
        String needle = "a";
        // String[] strs = {"ab", "a"};
        String[] strs = {"flower","flow","flight"};
        
        String ans = run.longestCommonPrefix(strs);
        System.out.println(ans);
        // System.out.println(Arrays.toString(ans));
        
        // ------------------------------

        long endTime = System.currentTimeMillis();
        System.out.println("Elapse of time: " + (endTime - startTime) +  " ms");
    }
    

    public String longestCommonPrefix(String[] strs) {

        for (int i = 0; i < strs[0].length(); i++) {
            char ch = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (strs[j].length() <= i || strs[j].charAt(i) != ch) {
                    return strs[0].substring(0,i);
                }
            }
        }
        return strs[0];
    
    }




    // ----------------------------------------------------------

}
