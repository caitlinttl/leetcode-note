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
        
        int ans = run.strStr(haystack, needle);
        System.out.println(ans);
        // System.out.println(Arrays.toString(ans));
        
        // ------------------------------

        long endTime = System.currentTimeMillis();
        System.out.println("Elapse of time: " + (endTime - startTime) +  " ms");
    }
    

    public int strStr(String haystack, String needle) {
        if (needle == "") {
            return 0;
        }
        if (!haystack.contains(needle)) {
            return -1;
        } else {
            return haystack.indexOf(needle);
        }
    }




    // ----------------------------------------------------------

}
