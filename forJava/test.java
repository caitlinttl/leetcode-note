public class test {

    public static void main(String[] args) {
        System.out.println("-----test java-----");
        test run = new test();

        System.out.println(run.rotateString("ddd", "ddd"));
    }

    public boolean rotateString(String s, String goal) {
        return s.length() == goal.length() && (s+s).contains(goal);
    }
}
