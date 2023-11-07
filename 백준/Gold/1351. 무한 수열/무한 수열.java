
import java.io.*;
import java.util.*;
public class Main {

    public static long N, P, Q;
    public static Map<Long, Long> infArr = new HashMap<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Long.parseLong(st.nextToken());
        P = Long.parseLong(st.nextToken());
        Q = Long.parseLong(st.nextToken());

        infArr.put(0L, 1L);

        System.out.println(dp(N));
    }

    public static long dp(long n) {
        if (infArr.getOrDefault(n, -1L) > -1) return infArr.get(n);

        infArr.put(n, dp((long)(n / P)) + dp((long)(n / Q)));

        return infArr.get(n);
    }
}
