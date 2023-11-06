
import java.io.*;
import java.util.*;
public class Main {

    public static int N;
    public static boolean[] visit;
    public static Map<Integer, Integer> tree;
    public static int result = 0;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        while (T > 0) {
            N = Integer.parseInt(br.readLine());
            tree = new HashMap<>();
            visit = new boolean[N + 1];
            result = 0;

            for (int i = 1; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                tree.put(b, a);
            }
            st = new StringTokenizer(br.readLine());
            int find1 = Integer.parseInt(st.nextToken());
            int find2 = Integer.parseInt(st.nextToken());

            dfs(find1);
            dfs(find2);

            sb.append(result);
            sb.append("\n");

            T--;
        }

        bw.write(sb.toString());

        bw.close();
        br.close();

    }

    public static void dfs(int now) {
        if (visit[now]){
            result = now;
            return;
        }
        visit[now] = true;
        if (tree.getOrDefault(now, -1) == -1) return;
        dfs(tree.get(now));
    }
}
