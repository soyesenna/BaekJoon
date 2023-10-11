
import java.io.*;
import java.math.BigInteger;
import java.util.*;
public class Main {

    public static int N;
    public static BigInteger[] table;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        table = new BigInteger[N + 1];
        BigInteger a = dpFunc(1);

        table = new BigInteger[N + 1];
        BigInteger b = dpFunc(2);

        BigInteger c = a.add(b);
        BigInteger res = c.remainder(BigInteger.valueOf(10007));

        System.out.println(res.toString());

    }

    public static BigInteger dpFunc(int n) {
        if (n == N) {
            return BigInteger.valueOf(1);
        } else if (n > N) {
            return BigInteger.valueOf(0);
        }

        if (table[n] != null) return table[n];
        table[n] = dpFunc(n + 1).add(dpFunc(n + 2));
        return table[n];
    }
}
