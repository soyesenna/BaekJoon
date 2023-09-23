package p2206;

import java.io.*;
import java.util.*;
public class MainFail {

    public static int N;
    public static int M;
    public static List<List<Integer>> walls = new ArrayList<>();
    public static int[][] space;
    public static List<List<Integer>> direction = List.of(
            List.of(-1, 0),
            List.of(0, 1),
            List.of(1, 0),
            List.of(0, -1)
    );
    public static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        space = new int[N][M];

        for (int i = 0; i < N; i++) {
            char[] tmp = br.readLine().toCharArray();
            for (int j = 0; j < M; j++) {
                int n = tmp[j] - '0';
                if (n == 1) walls.add(new ArrayList<>(List.of(i, j)));
                space[i][j] = n;
            }
        }

        for (List<Integer> wall : walls) {
            int wallR = wall.get(0);
            int wallC = wall.get(1);
            space[wallR][wallC] = 0;
            bfs();
            space[wallR][wallC] = 1;
        }

        if (result == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(result);
    }

    public static void bfs() {
        Deque<List<Integer>> queue = new ArrayDeque<>();
        boolean[][] visit = new boolean[N][M];
        //r, c, distance
        queue.add(new ArrayList<>(List.of(0, 0, 1)));
        visit[0][0] = true;

        int nowResult = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            List<Integer> now = queue.pollFirst();
            visit[now.get(0)][now.get(1)] = true;
            if (now.get(2) == nowResult) continue;

            for (List<Integer> dir : direction) {
                int nowR = now.get(0) + dir.get(0);
                int nowC = now.get(1) + dir.get(1);
                if (inRange(nowR, nowC) && !visit[nowR][nowC] && space[nowR][nowC] != 1) {
                    if (nowR == N - 1 && nowC == M - 1) nowResult = Math.min(nowResult, now.get(2) + 1);
                    queue.add(new ArrayList<>(List.of(nowR, nowC, now.get(2) + 1)));
                    visit[nowR][nowC] = true;
                }
            }
        }
        result = Math.min(nowResult, result);
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}
