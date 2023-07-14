public class MultipleCheck {
    public static void main(String[] args) {
        int N = 10;
        int M = 5;

        if (N % M == 0) {
            System.out.println(N + " is an exact multiple of " + M);
        } else {
            System.out.println(N + " is not an exact multiple of " + M);
        }
    }
}

