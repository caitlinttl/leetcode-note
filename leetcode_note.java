public class leetcode_note {

    // # 796. Rotate String Easy---------------------------------------
    class Solution {
        public boolean rotateString(String s, String goal) {
          return s.length() == goal.length() && (s+s).contains(goal);
        }
    }    
}
