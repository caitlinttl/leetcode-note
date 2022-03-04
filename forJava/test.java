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
        String s = "leetcode";
        String needle = "a";
        // String[] strs = {"ab", "a"};
        String[] strs = {"flower","flow","flight"};
        
        int ans = run.firstUniqChar(s);
        System.out.println(ans);
        // System.out.println(Arrays.toString(ans));
        
        // ------------------------------

        long endTime = System.currentTimeMillis();
        System.out.println("Elapse of time: " + (endTime - startTime) +  " ms");
    }
    

    public int firstUniqChar(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (s.indexOf(s.charAt(i)) == i && s.indexOf(s.charAt(i), i + 1) == -1 ) {
                return i;
            }
        }
        return -1;
    }




    // ----------------------------------------------------------

}
