
import java.io.*;
import java.util.*;
public class Main {

    public static int N, deleteNode, rootNode;
    public static Map<Integer, Set<Integer>> tree = new HashMap<>();
    public static boolean[] removed;


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) tree.put(i, new HashSet<>());
        removed = new boolean[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int now = Integer.parseInt(st.nextToken());
            if (now == -1) rootNode = now;
            else tree.get(now).add(i);
        }

        deleteNode = Integer.parseInt(br.readLine());
        removed[deleteNode] = true;
        dfs(deleteNode);

        int cnt = 0;
        for (Integer integer : tree.keySet()) {
            if (!removed[integer]) {
                boolean flag = true;
                for (Integer val : tree.get(integer)) {
                    if (!removed[val]){
                        flag = false;
                        break;
                    }
                }
                if (flag) cnt++;
            }
        }

        System.out.println(cnt);
    }

    public static void dfs(int root) {
        removed[root] = true;
        for (Integer now : tree.get(root)) {
            removed[now] = true;
            dfs(now);
        }
    }
}
