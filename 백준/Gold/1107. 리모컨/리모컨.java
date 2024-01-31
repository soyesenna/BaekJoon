
import java.io.*;
import java.util.*;

public class Main {

    private static int M;
    private static boolean[] buttons = new boolean[10];

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int dest = Integer.parseInt(br.readLine());

        M = Integer.parseInt(br.readLine());

        Arrays.fill(buttons, true);

        if (M > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                buttons[Integer.parseInt(st.nextToken())] = false;
            }
        }

        if (dest == 100) {
            System.out.println(0);
            System.exit(0);
        }
        
        if (M > 9){
            System.out.println(Math.abs(dest - 100));
            System.exit(0);
        }

        int count = 0;
        int result = 0;

        while (true){
            String min = String.valueOf(dest - count);
            String max = String.valueOf(dest + count);

            if (check(min)) {
                result += min.length();
                result += count;
                break;
            } else if (check(max)) {
                result += max.length();
                result += count;
                break;
            }
            count++;
        }
        System.out.println(Math.min(result, Math.abs(dest - 100)));

    }

    private static boolean check(String str){
        if (Integer.parseInt(str) < 0) return false;
        boolean result = true;
        for (int i = 0; i < str.length(); i++) {
            if (!buttons[Character.digit(str.charAt(i), 10)]) {
                result = false;
                break;
            }
        }

        return result;
    }

}
