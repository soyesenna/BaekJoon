
import java.io.*;
import java.util.*;
public class Main {

    public static int N, M;
    public static Map<Integer, Set<Integer>> friends = new HashMap<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            friends.put(i, new HashSet<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            friends.get(a).add(b);
            friends.get(b).add(a);
        }

        //System.out.println(friends);

        for (int i = 0; i < N; i++) {
            int result = dfs(i, 1, -1, new boolean[N]);
            if (result == 1) {
                System.out.println(1);
                System.exit(0);
                break;
            }
        }
        System.out.println(0);
    }

    public static int dfs(int num, int cnt, int parent, boolean[] visit) {
        if (cnt >= 5) return 1;

        int result = 0;
        visit[num] = true;
        for (Integer i : friends.get(num)) {
            if (i == parent) continue;
            if (visit[i]) continue;
            visit[i] = true;
            result = Math.max(dfs(i, cnt + 1, num, visit), result);
            visit[i] = false;
        }
        visit[num] = false;
        return result;
    }
}
