public class Busy {
  public static void main(String[] args) throws Exception {
    long end = System.currentTimeMillis() + 1500;
    long x = 0;
    while (System.currentTimeMillis() < end) {
      for (int i = 0; i < 100000; i++) { x += i % 7; }
    }
    System.out.println(x);
  }
}
