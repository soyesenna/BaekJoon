
import java.io.*;
import java.util.*;
public class Main {

    public static int N, M;
    public static int[][] space;
    public static int[][] table;
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public static boolean[][] visit;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        space = new int[N][M];
        table = new int[N][M];
        visit = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                space[i][j] = Integer.parseInt(st.nextToken());
                table[i][j] = -1;
            }
        }

        visit[0][0] = true;
        dfs(0, 0);
        System.out.println(table[0][0]);

    }


    public static int dfs(int r, int c) {
        if (r == N - 1 && c == M - 1) return 1;
        if (table[r][c] != -1) return table[r][c];

        table[r][c] = 0;
        visit[r][c] = true;
        for (List<Integer> dir : direction) {
            int nowR = r + dir.get(0);
            int nowC = c + dir.get(1);
            if (inRange(nowR, nowC) && !visit[nowR][nowC] && space[nowR][nowC] < space[r][c]) {
                visit[nowR][nowC] = true;
                table[r][c] += dfs(nowR, nowC);
                visit[nowR][nowC] = false;
            }
        }

        visit[r][c] = false;
        return table[r][c];
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}
