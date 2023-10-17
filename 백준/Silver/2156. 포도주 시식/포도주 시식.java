
import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static List<Integer> grape = new ArrayList<>();
    public static int[] dp;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        grape.add(0);

        for (int i = 0; i < N; i++) {
            grape.add(Integer.parseInt(br.readLine()));
        }

        dp = new int[N + 1];

        dp[1] = grape.get(1);
        if (N == 1) {
            System.out.println(dp[1]);
            System.exit(0);
        }
        dp[2] = grape.get(1) + grape.get(2);
        if (N == 2) {
            System.out.println(dp[2]);
            System.exit(0);
        }
        dp[3] = Math.max(Math.max(dp[1], grape.get(2)) + grape.get(3), dp[2]);

        for (int n = 4; n < N + 1; n++) {
            dp[n] = Math.max(Math.max(dp[n - 3] + grape.get(n - 1) + grape.get(n), dp[n - 2] + grape.get(n)), dp[n - 1]);
        }

        System.out.println(Arrays.stream(dp).max().getAsInt());
    }

}
