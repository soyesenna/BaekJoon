
import java.io.*;
import java.util.*;
public class Main {

    public static int[] dp;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        List<Integer> result = new ArrayList<>();

        while (T > 0) {
            //if (T == 0) break;
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            if (n == 1){
                result.add(1);
                T--;
                continue;
            } else if (n == 2) {
                result.add(2);
                T--;
                continue;
            } else if (n == 3) {
                result.add(4);
                T--;
                continue;
            }

            dp = new int[n + 1];
            dp[1] = 1;
            dp[2] = 2;
            dp[3] = 4;


            result.add(dpFunc(n));
            T--;
        }
        for (Integer integer : result) {
            System.out.println(integer);
        }
    }

    public static int dpFunc(int n) {
        int res = dp[n - 1] == 0 ? dpFunc(n - 1) : dp[n - 1];
            res += dp[n - 2] == 0 ? dpFunc(n - 2) : dp[n - 2];
            res += dp[n - 3] == 0 ? dpFunc(n - 3) : dp[n - 3];
        dp[n] += res;
        return res;
    }
}
