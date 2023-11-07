
import java.io.*;
import java.util.*;
public class Main {

    public static int N, M;
    public static final Map<Character, List<Integer>> charDirection = new HashMap<>();
    public static char[][] space;
    public static boolean[][] dp;
    public static boolean[][] ifMemorize;

    static {
        charDirection.put('U', List.of(-1, 0));
        charDirection.put('R', List.of(0, 1));
        charDirection.put('D', List.of(1, 0));
        charDirection.put('L', List.of(0, -1));
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        space = new char[N][M];
        dp = new boolean[N][M];
        ifMemorize = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            char[] tmp = br.readLine().toCharArray();
            space[i] = tmp;
        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (dfs(i, j)) result++;
            }
        }

        System.out.println(result);

    }

    public static boolean dfs(int r, int c) {
        if (!inRange(r, c)) return true;
        if (ifMemorize[r][c]) return dp[r][c];

        char nowDir = space[r][c];
        int nowR = r + charDirection.get(nowDir).get(0);
        int nowC = c + charDirection.get(nowDir).get(1);

        ifMemorize[r][c] = true;
        dp[r][c] = dfs(nowR, nowC);

        return dp[r][c];
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}
