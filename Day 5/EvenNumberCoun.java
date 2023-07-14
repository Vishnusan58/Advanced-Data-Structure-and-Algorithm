public class EvenNumberCount {
    public static void main(String[] args) {
        int[] numbers = {2, 5, 8, 11, 14};
        int evenCount = 0;

        for (int number : numbers) {
            if (number % 2 == 0) {
                evenCount++;
            }
        }

        System.out.println("The number of even numbers is: " + evenCount);
    }
}
