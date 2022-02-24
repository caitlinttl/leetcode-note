import java.util.Arrays;
import java.util.HashMap;

public class test {

    public static void main(String[] args) {
        System.out.println("-----test java-----");
        test run = new test();
        
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] ans = run.twoSum(nums, target);
        System.out.println(Arrays.toString(ans));
    }

    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i=0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff)) {
                ans[0] = map.get(diff);
                ans[1] = i;
                return ans;
            }

            map.put(nums[i], i);
        }

        return null;

    }


}
