public class EvenOddNumberCount {
    public static void main(String[] args) {
        int[] numbers = {2, 5, 8, 11, 14};
        int evenCount = 0;
        int oddCount = 0;

        for (int number : numbers) {
            if (number % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }

        System.out.println("The number of even numbers is: " + evenCount);
        System.out.println("The number of odd numbers is: " + oddCount);
    }
}
