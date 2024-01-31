
import java.io.*;

public class Main {

    private static boolean[] nums = new boolean[10001];

    public static void main(String[] args) throws IOException{

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int i = 1; i < 10001; i++) {
            String strNum = String.valueOf(i);
            int tmp = i;
            for (int j = 0; j < strNum.length(); j++) {
                tmp += Character.digit(strNum.charAt(j), 10);
            }
            if (tmp < 10001) nums[tmp] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < 10001; i++) {
            if (!nums[i]) {
                sb.append(i);
                sb.append("\n");
            }
        }

        bw.write(sb.toString());
        bw.flush();

        bw.close();
    }
}
