public class arrays {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        int length = numbers[2];
        char[] chars = new char[length];
        chars[numbers.length - 5] = 'y';
        System.out.println("Done!");
    }
}
