public class java_shr {
    public static void main(String[] args) {
        char num1 = 0xCC;

        System.out.printf("0x%X\n", num1 >> 2);
        System.out.printf("0x%X\n", ((byte)num1 >> 2));
    }
}
