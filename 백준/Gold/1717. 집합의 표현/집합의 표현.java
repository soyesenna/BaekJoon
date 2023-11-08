
import java.io.*;
import java.util.*;
public class Main {

    public static int N, M;
    public static int[] arr;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N + 1];
        init();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int order = Integer.parseInt(st.nextToken());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());

            if (order == 0) union(n1, n2);
            else {
                if (findRoot(n1) == findRoot(n2)) sb.append("YES");
                else sb.append("NO");
                sb.append("\n");
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(sb.toString());

        bw.close();
        br.close();
    }
    
    public static void init() {
        for (int i = 0; i <= N; i++) arr[i] = i;
    }

    public static void union(int n1, int n2) {
        n1 = findRoot(n1);
        n2 = findRoot(n2);
        if (n1 != n2) {
            arr[n1] = n2;
        }
    }

    public static int findRoot(int n) {
        if (n == arr[n]) return n;
        return arr[n] = findRoot(arr[n]);
    }
}
