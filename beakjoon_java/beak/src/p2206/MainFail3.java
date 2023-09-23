package p2206;

import java.io.*;
import java.util.*;

public class MainFail3 {

    public static int N;
    public static int M;
    public static int[][] space;
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public static int result = Integer.MAX_VALUE;
    public static boolean[][] visit;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        if (N == 1 && M == 1) {
            System.out.println(1);
            System.exit(0);
        }
        space = new int[N][M];
        visit = new boolean[N][M];
        visit[0][0] = true;

        for (int i = 0; i < N; i++) {
            char[] tmp = br.readLine().toCharArray();
            for (int j = 0; j < M; j++) {
                int n = tmp[j] - '0';
                space[i][j] = n;
            }
        }

        dfs(0, 0, 1, 0);
        if (result == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(result);

    }

    public static void dfs(int r, int c, int distance, int breakWall) {
        if (r == N - 1 && c == M - 1) {
            result = Math.min(distance, result);
            return;
        }
        if (breakWall > 1) {
            //visit[r][c] = false;
            return;
        }
        for (List<Integer> dir : direction) {
            int nowR = r + dir.get(0);
            int nowC = c + dir.get(1);
            if (inRange(nowR, nowC) && !visit[nowR][nowC]) {
                visit[nowR][nowC] = true;
                if (space[nowR][nowC] == 1) dfs(nowR, nowC, distance + 1, breakWall + 1);
                else dfs(nowR, nowC, distance + 1, breakWall);
                visit[nowR][nowC] = false;
            }
        }
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}